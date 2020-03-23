import requests


def get_users_json():
    headers = {
        'content-type' : 'application/x-www-form-urlencoded',
        'x-auth-token' : '62c679c0340cd0b1aca7b34099384f54'
    }
    url = 'https://userapi.webinar.ru/v3/organization/members'
    return requests.get(url, headers=headers).json()


def json_with_users():
    data = {}
    user_json = get_users_json()
    for obj in user_json:
        if 'Комнат' in obj['nickname']:
            data[obj['id']] = obj['nickname']
    list_d = list(data.items())
    list_d.sort(key=lambda i: i[1])
    return list_d


def start_to_vebinar(eventSessionId):
    url = f' https://userapi.webinar.ru/v3/eventsessions/{str(eventSessionId)}/start'
    answer = requests.put(url, headers=headers)
