import requests
import datetime
import sys
import time
from typing import List
from modules.consts.common import HEADERS
from modules.time_manager import converter_time
from modules.time_manager import converter_to_datetime
from datetime import timedelta
from modules.google_table.reader import read_table
from modules.google_table.updater import update_status


def manager_controller():
    """
    manager_controller() accepts 3 main parameters:
        1.  date_time: list[list]
                firts date_time in sub_list parameter must be date
                second date_time in sub_list parameter must be time
                    expamle:
                        [
                            [%Y-%m-%d, %H:%M],
                            [%Y-%m-%d, %H:%M]
                        ]

        2.  table_data: dict
                the following parameters should be in the dictionary:
                    2.1. 'Время по'
                    2.2. 'status'
                    2.3. 'Время с'
                    2.4  'event_session_id'

    """


    def control(current_time: datetime.datetime):
        table_data = read_table()
        for row in table_data:
            if (
                converter_to_datetime(
                    row['Время по']
                ) + datetime.timedelta(hours=1)
            ) < current_time:
                continue
            elif converter_to_datetime(
                row['Время по']
            ) <= (
                current_time - datetime.timedelta(minute=2)
            ) and row['status'] == 'active':
                vebinar_manager(event_session_id=row['event_session_id'] , param='stop')
                update_status(row=row['row'], status='finish')
            elif (
                converter_to_datetime(
                    row['Время с']
                ) - datetime.timedelta(minute=7)
            ) <= current_time and row['status'] == 'inactive':
                vebinar_manager(event_session_id=row['event_session_id'], param='start')
                update_status(row=row['row'], status='active')
            elif (
                converter_to_datetime(
                    row['Время с']
                ) - datetime.timedelta(hours=1)
            ) > current_time:
                break


    def get_start_time(current_time: datetime.datetime):
        if (current_time.minute % 2) != 0:
            current_time -= datetime.timedelta(minute=1)
        return current_time


    if date_time.__len__() != 2:
        print(manager_controller.__doc__)
        sys.exit()

    current_time = datetime.datetime.now()

    while True:
        if (current_time - datetime.timedelta(minute=2)) < get_start_time(current_time):
            time.sleep(10)
        else:
            current_time += datetime.timedelta(minute=2)
            control()


def vebinar_manager(event_session_id: str, param: str) -> None:
    """
    vebinar_manager() accepts two main parameters:
        1.  event_session_id: str,

        2.  param: str
                param can be 'start' or 'stop'
    """
    if param not in ["start", "stop"]:
        import sys
        print(vebinar_manager.__doc__)
        sys.exit()
    try:
        url = f' https://userapi.webinar.ru/v3/eventsessions/{str(event_session_id)}/{str(param)}'
        answer = requests.put(url, headers=HEADERS)
        if answer.status_code == 204:
            if param == "start":
                print(f"Webinar {event_session_id} was started")
            if param == "stop":
                print(f"Webinar {event_session_id} was stopped")
        else:
            print(f"Bad event_session_id: {event_session_id}")
            print(f"Answer: {answer}")
    except Exception as e:
        print(f"vebinar_manager() error: {e}")
        print(f"event_session_id: {event_session_id}")
        print(f"Type of event_session_id: {type(event_session_id)}")