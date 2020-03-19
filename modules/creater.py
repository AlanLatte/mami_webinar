# приходит dict
# вовзарщаю name, user_id, year, month, day, hour_s, minut_s

def create_event(name, user_id, year, month, day, hour_s, minut_s):
    url     =   'https://userapi.webinar.ru/v3/events'
    body    =   {
                    'name'                  :   str(name),
                    'access'                :   '1',
                    'startsAt[date][year]'  :   str(year),
                    'startsAt[date][month]' :   str(month),
                    'startsAt[date][day]'   :   str(day),
                    'startsAt[time][hour]'  :   str(hour_s),
                    'startsAt[time][minute]':   str(minut_s),
                    'lectorids'             :   str(user_id),
                    'ownerId'               :   str(user_id),
                    'type'                  :   'webinar',
                    'duration'              :   'PT1H30M0S',
                }
    answer = requests.post(url, data=body, headers=headers)
    print(answer.json())
    return answer.json()['eventId']

def create_event_session(event_id, name, year, month, day, hour_s, minute_s):
    url     =   f'https://userapi.webinar.ru/v3/events/{str(event_id)}/sessions'
    body    =   {
                    'name'                  :   str(name),
                    'access'                :   '1',
                    'lang'                  :   'RU',
                    'startsAt[date][year]'  :   str(year),
                    'startsAt[date][month]' :   str(month),
                    'startsAt[date][day]'   :   str(day),
                    'startsAt[time][hour]'  :   str(hour_s),
                    'startsAt[time][minute]':   str(minute_s),
                }

    answer = requests.post(url, data=body, headers=headers).json()
    print(answer)
    return answer['eventSessionId'], answer['link']