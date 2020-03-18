import requests
import json
from openpyxl import load_workbook
from common import ROOMS
from common import HEADERS as headers
from registrator import register_to_vebinar
from time_manager import conver_time

def change_path():
    import os
    os.chdir(
        os.path.realpath(
            os.path.join(
                os.getcwd(), os.path.dirname(file)
            )
        )
    )

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

def main(path):
    id      = 0
    sheet_  = wload_workbook(path)['Worksheet']
    row     = 2
    while True:
<<<<<<< HEAD
        year, month, day = conver_time(sheet_.cell(row = row, column = 1).value)
=======
        year, month, day = conver_time(str(sheet_.cell(row = row, column = 1).value))
>>>>>>> 8a568016b70c5c34ce4eeb898e3f662c1dc5837c
        name    = sheet_.cell(row = row, column = 3).value
        email   = sheet_.cell(row = row, column = 4).value
        subject = sheet_.cell(row = row, column = 6).value
        start_t = str(sheet_.cell(row=row, column=7).value).split(':')

        print(name,email,time,subject, start_t)

        else:
            event_id    = create_event(
                name    =   subject,
                user_id =   ROOMS[id][0],
                year    =   int(year),
                month   =   int(month),
                day     =   int(day),
                hour_s  =   int(start_t[0]),
                minut_s =   int(start_t[1])
            )

            event_session_id, link  = create_event_session(
                event_id    =   event_id,
                name        =   subject,
                year        =   int(year),
                month       =   int(month),
                day         =   int(day),
                hour_s      =   int(start_t[0]),
                minute_s    =   int(start_t[1])
            )

            register_to_vebinar(
                eventsessionID  =   event_session_id,
                name            =   name,
                email           =   email
            )

            sheet_.cell(row = row, column = 9).value = link
            sheet_.cell(row = row, column = 10).value = ROOMS[id][1]
            wb.save(path)

        if id+1 == len(ROOMS):
            id = 0
        else:
            id += 1
        row += 1
        if sheet_.cell(row = row, column = 1).value == None:
            break

if __name__ == '__main__':
    change_path()
    path = 'main__01.xlsx'
    main(path)
