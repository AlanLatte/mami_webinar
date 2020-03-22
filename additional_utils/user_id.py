import requests
from modules.consts.common import HEADERS


def get_all_users_id():
    url = "https://userapi.webinar.ru/v3/organization/members"
    return requests.get(url=url, headers=HEADERS).json()
