import datetime
import time

import requests

import log
from modules.consts.common import HEADERS
from modules.google_table.reader import read_table
from modules.google_table.updater import update_status
from modules.time_manager import converter_to_datetime

logger = log.get_logger(name="webinar_manager")


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
        try:
            table_data = read_table()
            for row in table_data:
                if (
                    converter_to_datetime(f"{row['Дата']} {row['Время по']}")
                    <= (current_time - datetime.timedelta(minutes=3))
                    and row["status"] == "active"
                ):
                    webinar_manager(
                        event_session_id=row["event_session_id"],
                        param="stop",
                        row_in_google_table=row["row"],
                    )
                elif (
                    converter_to_datetime(f"{row['Дата']} {row['Время с']}")
                    - datetime.timedelta(minutes=7)
                ) <= current_time and row["status"] == "inactive":
                    webinar_manager(
                        event_session_id=row["event_session_id"],
                        param="start",
                        row_in_google_table=row["row"],
                    )
                elif (
                    converter_to_datetime(f"{row['Дата']} {row['Время с']}")
                    - datetime.timedelta(hours=1)
                ) > current_time:
                    return True
        except:
            return False

    def get_start_time(current_time: datetime.datetime):
        if (current_time.minute % 2) != 0:
            current_time -= datetime.timedelta(minutes=1)
        return current_time

    current_time = get_start_time(datetime.datetime.now())
    logger.info("Init manager", start_time=datetime.datetime.now())
    control(datetime.datetime.now())
    while True:
        if (datetime.datetime.now() - datetime.timedelta(minutes=1)) < current_time:
            time.sleep(10)
        else:
            current_time += datetime.timedelta(minutes=2)
            logger.info("Control loop started")
            while True:
                response = control(datetime.datetime.now())
                if not response:
                    logger.info(
                        "Cant connect to google table.",
                        reason="All webinars are closed or "
                        "you have problem with ethernet",
                        timestamp=datetime.datetime.now(),
                    )
                    time.sleep(5)
                else:
                    break
            logger.info(
                "10 seconds delay started.", timestamp=datetime.datetime.now(),
            )
            time.sleep(10)


def webinar_manager(
    event_session_id: str, param: str, row_in_google_table: str
) -> None:
    """
    vebinar_manager() accepts two main parameters:
        1.  event_session_id: str,

        2.  param: str
                param can be 'start' or 'stop'
    """
    if param not in ["start", "stop"]:
        import sys

        print(webinar_manager.__doc__)
        sys.exit()
    try:
        url = f" https://userapi.webinar.ru/v3/eventsessions/{str(event_session_id)}/{str(param)}"
        answer = requests.put(url, headers=HEADERS)
        if answer.status_code == 204:
            if param == "start":
                update_status(row=row_in_google_table, status="active")
                logger.info("Webinar was started", event_session_id=event_session_id)
            if param == "stop":
                update_status(row=row_in_google_table, status="finish")
                logger.info("Webinar was stopped", event_session_id=event_session_id)
        elif answer.status_code == 404:
            if param == "start":
                update_status(row=row_in_google_table, status="active")
                logger.info(
                    "Webinar was started by teacher", event_session_id=event_session_id
                )
            if param == "stop":
                update_status(row=row_in_google_table, status="finish")
                logger.info(
                    "Webinar was stopped by teacher", event_session_id=event_session_id
                )
            logger.info(
                "Webinar was stopped by teacher", event_session_id=event_session_id
            )
        elif answer.status_code == 500:
            logger.info("Server get 500", answer=answer)
        else:
            logger.info(
                "Bad event_session_id", event_session_id=event_session_id, answer=answer
            )
    except Exception as e:
        logger.info(
            "vebinar_manager() error",
            error=e,
            event_session_id=event_session_id,
            type_even_session_id=type(event_session_id),
        )


if __name__ == "__main__":
    manager_controller()
