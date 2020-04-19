import requests
from modules.consts.common import ROOMS, INPUT_DIR_PATH
import os
import csv
import time


def worker(data):
    id = 0
    for webinar in data:
        # https://userapi.webinar.ru/v3/organization/events/{eventID}/move
        user_id = ROOMS[id][0]
        HEADERS = {
            "content-type": "application/x-www-form-urlencoded",
            "x-auth-token": "62c679c0340cd0b1aca7b34099384f54",
        }

        body = {"userId": user_id}
        print(webinar["eventId"])
        answer = requests.put(
            url=f'https://userapi.webinar.ru/v3/organization/events/{str(webinar["eventId"])}/move',
            data=body,
            headers=HEADERS,
        )
        print(answer)
        id += 1
        if id == len(ROOMS):
            id = 0

        time.sleep(1)


def reader():
    with open(
        os.path.join(INPUT_DIR_PATH, "svodniy_table.csv"), mode="r", encoding="utf-8"
    ) as csvfile:
        reader_ = csv.DictReader(csvfile, delimiter=";")
        for row in reader_:
            yield {"eventSessions": row["event_session_id"], "eventId": row["event_id"]}


if __name__ == "__main__":

    worker(reader())
