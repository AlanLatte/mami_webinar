import os
import sys
from openpyxl import load_workbook
from openpyxl import Workbook
from .consts.common import OUTPUT_DIR_PATH

def write_data(sheet_, wb, event_session_id, link, room, row, path):
    sheet_.cell(row = row, column = 9).value = link
    sheet_.cell(row = row, column = 10).value = room
    sheet_.cell(row = row, column = 15).value = event_session_id
    wb.save(path)

def create_workbook(data: list, name: str, params: dict):
    if params['type'] == "global":
        TITLE = tuple("Дата", "ID", "Преподаватель ФИО",\
            "Почта преподавателя", "Телефон преподавателя",\
            "Название предмета", "Время с", "Время по", "Ссылка",\
            "Вебинарная комната", "Группы")

    elif params['type'] == "local":
        TITLE = tuple("Дата", "ID", "Преподаватель ФИО",\
            "Почта преподавателя", "Телефон преподавателя",\
            "Название предмета", "Время с", "Время по", "Ссылка",\
            "Вебинарная комната", "Группы")
    else:
        print("create_workbook need some params!")
        sys.exit()

    OUTPUT_FILE_PATH = f"{OUTPUT_DIR_PATH}/{name}"
    if name not in os.listdir(OUTPUT_DIR_PATH):
        work_book = Workbook()
        work_book.save(filename = str(OUTPUT_FILE_PATH))

    work_book = load_workbook(OUTPUT_FILE_PATH)
    sheet_names = work_book.sheetnames
    if sheet_names.__len__() == 1:
        sheet = work_book[sheet_names[0]]
        for column, title_object in (TITLE):
            sheet.cell(row=int(1), column=int(column)+1).value =\
                title_object

        for row, data_object  in enumerate(data):
            for column, sub_obj in enumerate(data_object):
                sheet.cell(row = int(row)+2, column = int(column)+1).value =\
                    sub_obj
    work_book.save(filename = str(OUTPUT_FILE_PATH))
