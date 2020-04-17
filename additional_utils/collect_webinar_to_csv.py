import csv
import os
from typing import Dict, Iterable

from modules.consts.common import OUTPUT_DIR_PATH


def writer(data: Iterable[Dict[str, str]]):
    with open(
        os.path.join(OUTPUT_DIR_PATH, "collect_webinar_to_csv.csv"), mode="w"
    ) as csvfile:
        dict_writer = csv.DictWriter(
            csvfile, fieldnames=["startAt", "endAt", "user", "eventSessions", "eventId"]
        )
        dict_writer.writeheader()
        for object_ in data:
            dict_writer.writerow(object_)
