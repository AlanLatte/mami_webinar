import requests

from modules.consts.common import HEADERS


def chat_options(eventsessionID, params: dict = {}):
    """
        chat:
            off

        polls:
            on
    """
    if params["chat"] == "off":
        requests.put(
            url=f"https://userapi.webinar.ru/v3/eventsessions/{eventsessionID}/chat",
            data={"isModerated": "off"},
            headers=HEADERS,
        )
    if params["polls"] == "on":
        requests.put(
            url=f"https://userapi.webinar.ru/v3/eventsessions/{eventsessionID}/questions/moderate",
            data={"isModerated": "true"},
            headers=HEADERS,
        )
