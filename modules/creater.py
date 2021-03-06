import requests

from .consts.common import HEADERS
from .csv_files import append_to_csv_file


def create_event(params):
    url = "https://userapi.webinar.ru/v3/events"
    body = {
        "name": str(params["subject"]),
        "access": "1",
        "startsAt[date][year]": str(int(params["date"][0])),
        "startsAt[date][month]": str(int(params["date"][1])),
        "startsAt[date][day]": str(int(params["date"][2])),
        "startsAt[time][hour]": str(int(params["start_t"][0])),
        "startsAt[time][minute]": str(int(params["start_t"][1])),
        "lectorids": str(params["user_id"]),
        "ownerId": str(params["user_id"]),
        "type": "webinar",
        "duration": "PT1H30M0S",
    }

    try:
        print(
            f"""
    +=============================+
    Создан вебинар
        id: {str(params['id'])}
        предмет: {str(params['subject'])}
        {str(params['start_t'][0])} часов {str(params['start_t'][1])} минут
    +=============================+
            """
        )
        return requests.post(url, data=body, headers=HEADERS).json()["eventId"]

    except KeyError:
        print("\tВебинар не создался")
    except:
        print("\tОшибка в создании вебинара")


def create_event_session(params, event_id, filename: str):
    url = f"https://userapi.webinar.ru/v3/events/{str(event_id)}/sessions"
    body = {
        "name": str(params["subject"]),
        "access": "1",
        "lang": "RU",
        "startsAt[date][year]": str(int(params["date"][0])),
        "startsAt[date][month]": str(int(params["date"][1])),
        "startsAt[date][day]": str(int(params["date"][2])),
        "startsAt[time][hour]": str(int(params["start_t"][0])),
        "startsAt[time][minute]": str(int(params["start_t"][1])),
    }
    try:
        answer = requests.post(url, data=body, headers=HEADERS).json()
        append_to_csv_file(event_id, answer["eventSessionId"], filename=filename)
        print(
            f"""
    Создана сессия
        eventSessionId: {answer['eventSessionId']}
            """
        )
        return answer["eventSessionId"], answer["link"]
    except KeyError:
        print("\tСессия не создана")
    except:
        print("\tОшибка в создании сессии")
