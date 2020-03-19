def create_event(params, user_id):
    url     =   'https://userapi.webinar.ru/v3/events'
    body    =   {
                    'name'                  :   str(params[3]),
                    'access'                :   '1',
                    'startsAt[date][year]'  :   str(params[0]),
                    'startsAt[date][month]' :   str(params[1]),
                    'startsAt[date][day]'   :   str(params[2]),
                    'startsAt[time][hour]'  :   str(params[6][0]),
                    'startsAt[time][minute]':   str(params[6][1]),
                    'lectorids'             :   str(user_id),
                    'ownerId'               :   str(user_id),
                    'type'                  :   'webinar',
                    'duration'              :   'PT1H30M0S',
                }
    answer = requests.post(url, data=body, headers=headers)
    return answer.json()['eventId']

def create_event_session(params, event_id):
    url     =   f'https://userapi.webinar.ru/v3/events/{str(event_id)}/sessions'
    body    =   {
                    'name'                  :   str(params[3]),
                    'access'                :   '1',
                    'lang'                  :   'RU',
                    'startsAt[date][year]'  :   str(params[0]),
                    'startsAt[date][month]' :   str(params[1]),
                    'startsAt[date][day]'   :   str(params[2]),
                    'startsAt[time][hour]'  :   str(params[6][0]),
                    'startsAt[time][minute]':   str(params[6][1]),
                }

    answer = requests.post(url, data=body, headers=headers).json()
    return answer['eventSessionId'], answer['link']
