import requests
import json
from openpyxl import load_workbook
from modules.consts.common import ROOMS
from modules.consts.common import HEADERS as headers
from modules.registrator import register_to_vebinar
from modules.time_manager import converter_date
from modules.writer import write_data, create_workbook
from modules.reader import read_all_info
from modules.creater import create_event, create_event_session
from modules.registrator import register_to_vebinar
from modules.utils.checker import check_required_folders
from modules.manager import vebinar_manager


from modules.google_table.reader import read_cells
from modules.google_table.writer import create_new_sheet


def main(mode: str) -> None:

    """TODO:
    1.  закинуть ключи к таблице в реп
    2.  удалить ненужные функции
    3.  называть переменные нормально. Отражать суть. (INFO -- не годится;) )
    4.  подключать logging
    5.  сделать функцию сортировки, которая будет позволять пропустить 0 в начале
    6.  прописать __doc__ важным функциям
    """

    id = 0
    info, id_to_book = read_all_info()
    info = sorted(info, key=lambda info: info[1], reverse = False)
    info = [i[0] for i in info]
    print(info)
    for row_info in info:
        row_info['user_id'] = ROOMS[id][0]
        row_info['room'] = ROOMS[id][1]

        if mode == 'online':
            row_info['event_id'] = create_event(row_info)
            row_info['event_session_id'], row_info['link'] = \
                create_event_session(row_info, row_info['event_id'])
        else:
            row_info['event_id'] = 'test'
            row_info['event_session_id'] = 'test'
            row_info['link'] = 'test'

        register_to_vebinar(eventsessionID=row_info['event_session_id'], params=row_info, mode=mode)

        id+=1
        if id == len(ROOMS):
            id = 0

    create_workbook(data=info, name='svodniy_table.xlsx', params={'type':'private'})
    result_books_names = []
    for file_name in id_to_book.values():
        if file_name not in result_books_names:
            result_books_names.append(file_name)
            temp_list = []
            for row in info:
                if id_to_book[row['id']] == file_name:
                    temp_list.append(row)
            create_workbook(data=temp_list, name=f'результат_{file_name}', params={'type':'public'})


if __name__ == '__main__':
    # check_required_folders()
    # mode = input('Выбирите режим работы: \t')
    # if mode == 'online' or mode == '1':
    #     print('online mode on\n')
    #     main('online')
    # else:
    #     print('offline mode on\n')
    #     main('offline')
    info, id_to_book = read_all_info()
    info = sorted(info, key=lambda info: info[1], reverse = False)
    info = [i[0] for i in info]
    print(info)
    for row_info in info:
        row_info['user_id'] = 'test'
        row_info['room'] = 'test'
        row_info['event_id'] = 'test'
        row_info['event_session_id'] = 'test'
        row_info['link'] = 'test'

    print(read_cells())
    # create_new_sheet(info=info)
    # vebinar_manager(event_session_id = '3598709', param='stop')
    print(main.__doc__)
