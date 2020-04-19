from modules.consts.common import ROOMS
from modules.registrator import register_to_vebinar
from modules.writer import create_workbook
from modules.reader import read_all_info
from modules.creater import create_event, create_event_session
from modules.registrator import register_to_vebinar
from modules.utils.checker import check_required_folders
from modules.manager import vebinar_manager

from modules.email.mail import send_all

from modules.google_table.reader import read_table
from modules.google_table.writer import create_new_sheet, create_virtual_table

from additional_utils.irrelevant_functions import json_with_users

from modules.google_table.updater import update_status
from modules.manager import manager_controller
from modules.settings import chat_options


def main(mode: str) -> None:
    """TODO:
    1.  удалить ненужные функции
    2.  называть переменные нормально. Отражать суть. (INFO -- не годится;) )
    3.  подключать logging
    4.  сделать функцию сортировки, которая будет позволять пропустить 0 в начале
    5.  прописать __doc__ важным функциям
    """

    room_id = 0
    info, id_to_book, file_to_email = read_all_info()
    info = sorted(info, key=lambda info: info[1], reverse=False)
    info = [i[0] for i in info]
    # print(info)
    for row_info in info:
        row_info["user_id"] = ROOMS[room_id][0]
        row_info["room"] = ROOMS[room_id][1]

        if mode == "online":
            row_info["event_id"] = create_event(row_info)
            row_info["event_session_id"], row_info["link"] = create_event_session(
                row_info, row_info["event_id"]
            )
        else:
            row_info["event_id"] = "test"
            row_info["event_session_id"] = "test"
            row_info["link"] = "test"

        if mode == "online":
            register_to_vebinar(
                eventsessionID=row_info["event_session_id"], params=row_info, mode=mode
            )

        room_id += 1
        if room_id == len(ROOMS):
            room_id = 0

    create_workbook(data=info, name="svodniy_table.xlsx", params={"type": "private"})
    result_books_names = []

    for file_name in id_to_book.values():
        if file_name not in result_books_names:
            result_books_names.append(file_name)
            temp_list = []
            for row in info:
                if id_to_book[row["id"]] == file_name:
                    temp_list.append(row)
            create_workbook(data=temp_list, name=file_name, params={"type": "public"})

    if mode == "online":
        print("создаётся google docs")
        try:
            create_new_sheet(info=info)
        except:
            print("уже существует google docs sheet на это число")
        else:
            print("создался google docs")
        print("отправляются письма")
        send_all(file_to_email)


if __name__ == "__main__":
    check_required_folders()
    mode = input("Выбирите режим работы: \t")
    if mode == "online" or mode == "1":
        print("online mode on\n")
        main("online")
    else:
        print("offline mode on\n")
        main("offline")

    print(main.__doc__)
