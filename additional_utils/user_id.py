from pprint import pprint
from typing import Tuple, List

import requests
from modules.consts.common import HEADERS


def get_all_users_id():
    url = "https://userapi.webinar.ru/v3/organization/members"
    return requests.get(url=url, headers=HEADERS).json()


def get_rooms() -> List[Tuple[int, str]]:
    rooms = [
        (item["id"], f'W{item["secondName"]}')
        for item in get_all_users_id()
        if item["name"].lower() == "комната"
    ]
    return sorted(rooms, key=lambda x: x[1])
