def create_event(params: dict):
    url     =   'https://userapi.webinar.ru/v3/events'
    body    =   {
                    'name'                  :   str(params['name']),
                    'access'                :   '1',
                    'startsAt[date][year]'  :   str(params['user_id']),
                    'startsAt[date][month]' :   str(params['year']),
                    'startsAt[date][day]'   :   str(params['day']),
                    'startsAt[time][hour]'  :   str(params['hour_s']),
                    'startsAt[time][minute]':   str(params['minut_s']),
                    'lectorids'             :   str(params['user_id']),
                    'ownerId'               :   str(params['user_id']),
                    'type'                  :   'webinar',
                    'duration'              :   'PT1H30M0S',
                }
    answer = requests.post(url, data=body, headers=headers)
    return answer.json()['eventId']

def create_event_session(params: dict):
    url     =   f'https://userapi.webinar.ru/v3/events/{str(event_id)}/sessions'
    body    =   {
                    'name'                  :   str(params['name']),
                    'access'                :   '1',
                    'lang'                  :   'RU',
                    'startsAt[date][year]'  :   str(params['year']),
                    'startsAt[date][month]' :   str(params['month']),
                    'startsAt[date][day]'   :   str(params['day']),
                    'startsAt[time][hour]'  :   str(params['hour_s']),
                    'startsAt[time][minute]':   str(params['minute_s']),
                }

    answer = requests.post(url, data=body, headers=headers).json()
    return answer['eventSessionId'], answer['link']
