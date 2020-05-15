import requests
from .consts.common import HEADERS


def register_to_vebinar(eventsessionID, params, mode):

    """role — роль участника на этом мероприятии. Значения:
- ADMIN
- LECTURER
- GUEST
    """

    url = f"https://userapi.webinar.ru/v3/eventsessions/{str(eventsessionID)}/register"
    names = name_refactor(params["name"])
    emails = email_refactoring(params["email"])
    for id in range(len(names)):
        try:
            if names[id] == "" or emails[id] == "":
                continue
            body = {
                "name": str(names[id]),
                "role": "ADMIN",
                "email": str(emails[id]),
            }
            if mode == "online":
                print(requests.post(url, data=body, headers=HEADERS).json())
            else:
                print(
                    f"\tРегистрация успешна {str(names[id])} \
email: {str(emails[id])}"
                )
        except:
            print(f"\tПроизошла ошибка регистрации пользователя")


def name_refactor(name):
    name = name.split("|")
    return name


def email_refactoring(email):
    try:
        email = email.replace(" ", "")
        email = email.split("|")
    except:
        email = "4.leo.makarov@gmail.com"
    return email
