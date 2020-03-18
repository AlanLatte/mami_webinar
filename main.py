import requests
import json
from openpyxl import load_workbook
import xlrd, xlwt

def get_users_json():
    url = 'https://userapi.webinar.ru/v3/organization/members'
    headers = {'content-type': 'application/x-www-form-urlencoded', 'x-auth-token':'62c679c0340cd0b1aca7b34099384f54'}
    r = requests.get(url, headers=headers)
    return r.json()

def json_with_users():
    json_ = {}

    json = get_users_json()
    for obj in json:
        if 'Комнат' in obj['nickname']:
            json_[obj['id']] = obj['nickname']
    list_d = list(json_.items())
    list_d.sort(key=lambda i: i[1])
    return list_d

def creater_event(url, body, headers):
    r = requests.post(url, data=body, headers=headers)
    print(r.json())

def create_event(name, user_id, year, month, day, hour_s, minut_s):
    url = 'https://userapi.webinar.ru/v3/events'
    body = {    'name': str(name), 'access':'1',
                'startsAt[date][year]':str(year),
                'startsAt[date][month]':str(month),
                'startsAt[date][day]':str(day),
                'startsAt[time][hour]':str(hour_s),
                'startsAt[time][minute]':str(minut_s),
                'lectorids':str(user_id),
                'ownerId':str(user_id),
                'type':'webinar',
                'duration': 'PT1H30M0S',
    }

    headers = {'content-type': 'application/x-www-form-urlencoded', 'x-auth-token':'62c679c0340cd0b1aca7b34099384f54'}
    r = requests.post(url, data=body, headers=headers)
    print(r.json())
    return r.json()['eventId']

def create_event_session(event_id, name, year, month, day, hour_s, minute_s):
    url = f'https://userapi.webinar.ru/v3/events/{str(event_id)}/sessions'

    headers = { 'content-type': 'application/x-www-form-urlencoded',
                'x-auth-token':'62c679c0340cd0b1aca7b34099384f54'
            }

    body = {
        'name':str(name),
        'access':'1',
        'lang' :'RU',
        'startsAt[date][year]':str(year),
        'startsAt[date][month]':str(month),
        'startsAt[date][day]':str(day),
        'startsAt[time][hour]':str(hour_s),
        'startsAt[time][minute]':str(minute_s),
    }

    r = requests.post(url, data=body, headers=headers)
    print(r.json())
    return r.json()['eventSessionId'], r.json()['link']

def register_to_vebinar(eventsessionID, name, email):
    url = f'https://userapi.webinar.ru/v3/eventsessions/{str(eventsessionID)}/register'

    headers = { 'content-type': 'application/x-www-form-urlencoded',
                'x-auth-token':'62c679c0340cd0b1aca7b34099384f54'}

    body = {
                'name':str(name),
                'role': 'LECTURER',
                'email':str(email),
    }

    r = requests.post(url, data=body, headers=headers)
    print(r.json())

def start_to_vebinar(eventSessionId):
    headers = { 'content-type': 'application/x-www-form-urlencoded',
                'x-auth-token':'62c679c0340cd0b1aca7b34099384f54'}

    url = f' https://userapi.webinar.ru/v3/eventsessions/{str(eventSessionId)}/start'
    r = requests.put(url, headers=headers)

def work_with_file(path):
    json_ = json_with_users()
    id = 0
    hour_ = 9

    wb = load_workbook(path)
    sheet_ = wb['Worksheet']
    row = 2
    while True:
        time = [2020, 3, 18]
        year = time[0]
        month = time[1]
        day = time[2]
        name = sheet_.cell(row=row, column=3).value
        email = sheet_.cell(row=row, column=4).value
        subject = sheet_.cell(row=row, column=6).value
        start_t = str(sheet_.cell(row=row, column=7).value).split(':')

        print(name,email,time,subject, start_t)
        if id == len(json_):
            sheet_.cell(row=row, column=11).value = 'Нет мест'
        else:
            book = xlwt.Workbook(encoding="utf-8")
            event_id = create_event(name=subject, user_id=json_[id][0], year=int(year), month=int(month), day=int(day), hour_s=int(start_t[0]), minut_s=int(start_t[1]))
            event_session_id, link = create_event_session(event_id=event_id, name=subject,  year=int(year), month=int(month), day=int(day), hour_s=int(start_t[0]), minute_s=int(start_t[1]))
            register_to_vebinar(eventsessionID=event_session_id, name=name, email=email)

            sheet_.cell(row=row, column=10).value = link
            sheet_.cell(row=row, column=11).value = json_[id][1]
            wb.save(path)

        if int(start_t[0]) != int(hour_):
            id = 1
            hour_ = start_t[0]
        else:
            id += 1
        row += 1
        if sheet_.cell(row=row, column=1).value == None:
            break

if __name__ == '__main__':
    path = 'main__01.xlsx'
    work_with_file(path)