
import logging
import ecs_logging
from time import time, sleep
from random import randint


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(f"logs/{int(time())}.log")
handler.setFormatter(ecs_logging.StdlibFormatter())
logger.addHandler(handler)

print("Generating log entries ...")

messages = [
    "Elvis has left the building",
    "Elvis has left the oven on",
    "Elvis has two left feet",
    "Elvis was left out in the cold",
    "Elvis was left holding the baby",
    "Elvis left the cake out in the rain",
    "Elvis came out of left field",
    "Elvis exited stage left",
    "Elvis took a left turn",
    "Elvis left no stone unturned",
    "Elvis picked up where he left off",
    "Elvis's train has left the station"
]

# Separated by "." extra generates nested JSON
while True:
    N, timeout = randint(0,15), randint(1,10)
    if N > 11:
        N = 0
    if N <= 4:
        logger.info(messages[N], extra={"http.request.body.content": messages[N]})
    elif 5 <= N <= 8:
        logger.warning(messages[N], extra={"http.request.body.content": messages[N]})
    elif 9 <= N <= 10:
        logger.error(messages[N], extra={"http.request.body.content": messages[N]})
    else:
        logger.critical(messages[N], extra={"http.request.body.content": messages[N]})
    sleep(timeout)
