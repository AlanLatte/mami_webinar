import requests
import json
from openpyxl import load_workbook
from modules.consts.common import ROOMS
from modules.consts.common import HEADERS as headers
from modules.registrator import register_to_vebinar
from modules.time_manager import converter_time
from modules.writer import write_data
from modules.writer import create_workbook
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


def main(mode: str):
    id = 0
    info, id_to_book = read_all_info()
    info = sorted(info, key=lambda info: info[1], reverse = False)
    # TODO: сделать функцию сортировки, которая будет полволять
    # пропустить 0 в начале
    info = [i[0] for i in info]
    print(info)
    for row_info in info:
        row_info['user_id'] = ROOMS[id][0]
        row_info['room'] = ROOMS[id][1]
        if mode == 'online':
            row_info['event_id'] = create_event(row_info)
            row_info['event_session_id'], row_info['link'] = \
                create_event_session(row_info, row_info['event_id'])
            register_to_vebinar(eventsessionID=row_info['event_session_id'], name=row_info['name'], email=row_info['email'])
        else:
            row_info['event_id']            = 'test'
            row_info['event_session_id']    = 'test'
            row_info['link']                = 'test'

        id+=1
        if id == len(ROOMS):
            id = 0

    create_workbook(data=info, name='svodniy_table.xlsx', params={'type':'dev'})
    result_books_names = []
    for file_name in id_to_book.values():
        if file_name not in result_books_names:
            result_books_names.append(file_name)
            temp_list = []
            for row in info:
                if id_to_book[row['id']] == file_name:
                    temp_list.append(row)
            create_workbook(data=temp_list, name=f'результат_{file_name}', params={'type':'stud'})


    # one = []
    # two = []
    # for row_info in info:
    #     if row_info[7] == 'Коломна':
    #         one.append(row_info)
    #     else:
    #         two.append(row_info)
    #
    # create_workbook(data=one, name="info_stud.xlsx", params={"type": "stud"})
    # create_workbook(data=info, name="info_dev.xlsx", params={"type": "dev"})


if __name__ == '__main__':
    # change_path(file)
    main('online')
