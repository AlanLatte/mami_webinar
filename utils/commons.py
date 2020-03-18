
def get_users_json():
    url     = 'https://userapi.webinar.ru/v3/organization/members'
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
    url     = f' https://userapi.webinar.ru/v3/eventsessions/{str(eventSessionId)}/start'
    answer  = requests.put(url, headers=headers)
