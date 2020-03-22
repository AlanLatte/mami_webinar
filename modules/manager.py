import requests
from modules.consts.common import HEADERS as headers

def vebinar_manager(event_session_id: str, param: str):
    """
    vebinar_manager() accepts two main parameters:
        event_session_id: str,
        param: str
            param can be 'start' or 'stop'
    """
    if param not in ["start", "stop"]:
        import sys
        print(vebinar_manager.__doc__)
        sys.exit()
    try:
        url = f' https://userapi.webinar.ru/v3/eventsessions/{str(event_session_id)}/{str(param)}'
        answer = requests.put(url, headers=headers)
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
