from datetime import datetime


def create_csv_file(filename: str):
    with open(filename, mode="w") as file:
        file.write("")


def create_file_name():
    return datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + ".csv"


def append_to_csv_file(event_id: str, event_session_id: str, filename: str) -> None:
    with open(filename, mode="a") as file:
        file.write(f"{event_id}, {event_session_id}\n")
