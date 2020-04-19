import requests
import datetime


import csv
import os
from typing import Dict, Iterable

from modules.consts.common import OUTPUT_DIR_PATH


def get_vebinars():
    HEADERS = {
        'content-type': 'application/x-www-form-urlencoded',
        'x-auth-token': '62c679c0340cd0b1aca7b34099384f54',
    }

    body = {
        'perPage': '250',
    }

    count = 0

    for userID in [19417123, 19417159]:
        for event in requests.get(f'https://userapi.webinar.ru/v3/users/{userID}/events/schedule', params=body, headers=HEADERS).json():
            for event in event['eventSessions']:
                yield {"startAt":str(event['startsAt']),
                       "endAt":None,
                       "subject":str(event['name']),
                       "eventSessions":str(event['id']),
                       "eventId":str(event['eventId']),
                }


def deleter(data: Iterable[Dict[str, str]]):
    for event in data:
        requests.delete(url=f'https://userapi.webinar.ru/v3/organization/events/{event["eventId"]}')


def writer(data: Iterable[Dict[str, str]]):
    with open(
        os.path.join(OUTPUT_DIR_PATH, "collect_webinar_to_csv.csv"), mode="w"
    ) as csvfile:
        dict_writer = csv.DictWriter(
            csvfile, fieldnames=["startAt", "endAt", "subject", "eventSessions",
                                 "eventId"]
        )
        dict_writer.writeheader()
        for object_ in data:
            dict_writer.writerow(object_)

if __name__ == '__main__':
    deleter(get_vebinars())
