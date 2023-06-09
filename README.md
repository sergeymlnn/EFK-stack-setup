# Intro
The goal of the project is to provide the most straightforfard way to connect & configure EFK (Elasticsearch, Filebeat, Kibana) stack to easily parse logs of your apps.
Before we go to the installation & usage details, it's worth mentioning that the following versions of EFK-stack are used in this project:
  - Elasticsearch 6.6.0
  - Filebeat 6.6.0
  - Kibana 6.6.0


# Installation
Besides **Docker**, **Docker-compose** is also *required* to configure & run the services. **Python** is *optional*. It's only used to generate logs to be parsed by simply running the [script](logs_generator.py). But don't forget to setup integration with [ecs-logging](https://www.elastic.co/guide/en/ecs-logging/python/current/installation.html).


## System Requirements

**Note**: other versions are also allowed, though ones below were using during development of the project. Feel free to adjust & test it in your environment carefully.

 - Docker: 20.10.12
 - Docker-Compose: 1.29.2
 - Python: 3.6.8

# Usage

Once the environment is prepared, we're going to run EFK-services like this: `docker-compose up`. If you don't care about output, append `-d` flag to the `docker-compose` instruction. A common way to check if Filebeat & Elasticsearch are connected is to run the following command:

```
docker exec -it docker-filebeat curl http://docker-elasticsearch:9200
```

If the response displays info about ES-cluster, like this

```json
{
  "name" : "U-glycs",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "PWXB9NIXQLeMezgre9pwqQ",
  "version" : {
    "number" : "6.6.0",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "a9861f4",
    "build_date" : "2019-01-24T11:27:09.439740Z",
    "build_snapshot" : false,
    "lucene_version" : "7.6.0",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}

```

then everything's OK. Alternatively, there's an option to check status of the container by using *docker-inspect* command: 

```
docker inspect docker-elasticsearch -f '{{ .State.Health.Status }}'
```

The expected output must be **healthy**. In other scenarios, please check the output of the docker-services for more details.

Before we start working with [Kibana](http://localhost:5601), you can execute the [script](logs_generator.py) to be running on the background, so you will have sample logs to play with.


## Kibana. Index Pattern & Logs Visualization
Kibana requires an index pattern to access the Elasticsearch data. An index pattern selects the data to use & allows to define properties of the fields. For example, an index pattern can point to log data from yesterday, or all indices that contain data. So let's create an index pattern & visulize our logs step by step.

### Step 1. Create an Index Pattern
Open [Kibana](http://localhost:5601) in a web browser, go to **Discover** section & select the name of the index that we specified in [filebeat.yml](filebeat.yml). Then create an *Index Pattern* for this index:

[![Step1.png](https://i.postimg.cc/ZnM1KGJj/Step1.png)](https://postimg.cc/D41CxYJb)

### Step 2. Create the First Diagram
Similarly to the previous step, switch back to the sidebar, then go to **Dashboard** section & *Create new dashboard* of a preferred type. As an example we're going to create a Vertical Bar diagram to visualize the number of entries in the log files of each particular level accordingly: *info*, *warning*, *error*, *critical*.

[![Step2.png](https://i.postimg.cc/MHh7d5Wd/Step2.png)](https://postimg.cc/QKJKMpKT)


### Step 3. Customize the Diagram
Once Filebeat successfully loaded data from the log files into the index & we created an <strike>unattractive</strike> prororype of a Vetical Bar, we need
to customize it a little bit in order to display a representable diagram. 

[![Step3.png](https://i.postimg.cc/L8XrwBM2/Step3.png)](https://postimg.cc/7fFsTz6W)


### Step 4. View & Save the Diagram
Last things last we need to save what we've done so far. Move your cursor to the top of the page & click **Save**. Provide a preferred name & that's pretty much it. Now you can continue customizing the diagram or create a new one. 

[![Step4.png](https://i.postimg.cc/W3y1Qbd1/Step4.png)](https://postimg.cc/9RG292P6)


# Conclusion
The implementation provides a quite simple approach to configure EFK-stack to parse logs of your apps. There are many other techniques & strategies you can investigate & use. A future plan is to design a one-point API to randomly generate logs just like the [script](logs_generator.py), but there we're going to configure EFK-stack in a way to read logs directly from stdout of the container with the API.  


# Useful Links
  - [Filebeat. Installation](https://www.elastic.co/guide/en/ecs-logging/python/current/installation.html)
  - [Run Filebeat on Docker](https://www.elastic.co/guide/en/beats/filebeat/current/running-on-docker.html)
  - [Ingest logs from a Python application using Filebeat](https://www.elastic.co/guide/en/cloud/current/ec-getting-started-search-use-cases-python-logs.html)
  - [Configure the Elasticsearch output](https://www.elastic.co/guide/en/beats/filebeat/current/elasticsearch-output.htm)
  - [Configure Elasticsearch index template loading](https://www.elastic.co/guide/en/beats/filebeat/current/configuration-template.html)
  - [Index Patterns](https://www.elastic.co/guide/en/kibana/6.6/index-patterns.html)
