import datetime


def converter_date(date):
    date_ = str(date).split("-")
    return [date_[0], date_[1], date_[2]]


def converter_time(time):
    return time.split(":")


def converter_to_datetime(date_time):
    return datetime.datetime.strptime(f"{date_time}", "%Y-%m-%d %H:%M")
