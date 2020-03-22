from .consts.common import HEADERS as headers
import requests

def create_event(params):
    url = 'https://userapi.webinar.ru/v3/events'
    body = {
                'name': str(params['subject']),
                'access': '1',
                'startsAt[date][year]': str(int(params['date'][0])),
                'startsAt[date][month]': str(int(params['date'][1])),
                'startsAt[date][day]': str(int(params['date'][2])),
                'startsAt[time][hour]': str(int(params['start_t'][0])),
                'startsAt[time][minute]': str(int(params['start_t'][1])),
                'lectorids': str(params['user_id']),
                'ownerId': str(params['user_id']),
                'type': 'webinar',
                'duration': 'PT1H30M0S',
            }
    answer = requests.post(url, data=body, headers=headers)
    try:
        print('+======+\n+======+\n')
        print(f"Создан вебинар \
    \n\tid: {str(params['id'])}\n\tпредмет: {str(params['subject'])}\
    \n\t{str(params['start_t'][0])} часов")
        return answer.json()['eventId']
    except KeyError:
        print('\tВебина не создался')
    except:
        print('\tОшибка в создании вебинара')


def create_event_session(params, event_id):
    url = f'https://userapi.webinar.ru/v3/events/{str(event_id)}/sessions'
    body = {
                'name': str(params['subject']),
                'access': '1',
                'lang': 'RU',
                'startsAt[date][year]': str(int(params['date'][0])),
                'startsAt[date][month]': str(int(params['date'][1])),
                'startsAt[date][day]': str(int(params['date'][2])),
                'startsAt[time][hour]': str(int(params['start_t'][0])),
                'startsAt[time][minute]': str(int(params['start_t'][1])),
            }

    answer = requests.post(url, data=body, headers=headers).json()
    try:
        print('\tСоздана сессия')
        return answer['eventSessionId'], answer['link']
    except KeyError:
        print('\tСессия не создана')
    except:
        print('\tОшибка в создании сессии')
