import requests
import json
from openpyxl import load_workbook
from modules.consts.common import ROOMS
from modules.consts.common import HEADERS as headers
from modules.registrator import register_to_vebinar
from modules.time_manager import converter_time
from modules.writer import write_data
from modules.reader import read_all_info
from modules.creater import create_event, create_event_session
from modules.registrator import register_to_vebinar

def change_path(file: str) -> None:
    import os
    os.chdir(
        os.path.realpath(
            os.path.join(
                os.getcwd(), os.path.dirname(file)
            )
        )
    )

def main():
    id = 0
    info = read_all_info()
    info = sorted(info, key=lambda info: info[6], reverse = False)
    for i in info:
        print(i)
        
    for params in info:
        event_id = create_event(params, ROOMS[0][0])
        event_session_id = create_event_session(params, event_id)
        register_to_vebinar(event_session_id, params[3], params[4])




if __name__ == '__main__':
    # file = 'main__03.xlsx'
    # change_path(file)
    main()
    pass
