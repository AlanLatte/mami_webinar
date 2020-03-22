import requests
from .consts.common import HEADERS as headers


def register_to_vebinar(eventsessionID, params, mode):

    """role — роль участника на этом мероприятии. Значения:
- ADMIN
- LECTURER
- GUEST
    """

    url = f'https://userapi.webinar.ru/v3/eventsessions/{str(eventsessionID)}/register'
    names = name_refactor(params['name'])
    emails = email_refactoring(params['email'])
    for id in range(len(names)):
        try:
            if names[id] == '' or emails[id] == '':
                continue
            body = {
                'name': str(names[id]),
                'role': 'ADMIN',
                'email': str(emails[id]),
            }
            if mode == 'online':
                print(requests.post(url, data=body, headers=headers).json())
            else:
                print(f"   Регистрация успешна {str(names[id])},
                \email {str(emails[id])}")
        except:
            print(f"   Произошла ошибка регистрации для пользователя {str(names[id])},\
             email {str(emails[id])}")


def name_refactor(name):
    name = name.split('|')
    return name


def email_refactoring(email):
    email = email.replace(' ', '')
    email = email.split('|')
    return email
