import os
from openpyxl import load_workbook
from openpyxl import Workbook
from modules.consts.common import OUTPUT_DIR_PATH

def write_data(sheet_, wb, event_session_id, link, room, row, path):
    sheet_.cell(row = row, column = 9).value = link
    sheet_.cell(row = row, column = 10).value = room
    sheet_.cell(row = row, column = 15).value = event_session_id
    wb.save(path)


def create_workbook(data: list, name: str):
    OUTPUT_FILE_PATH = f"{OUTPUT_DIR_PATH}/{name}"
    if name not in os.listdir(OUTPUT_DIR_PATH):
        work_book = Workbook()
        work_book.save(filename = str(OUTPUT_FILE_PATH))

    work_book = load_workbook(OUTPUT_FILE_PATH)
    sheet_names = work_book.sheetnames
    if sheet_names.__len__() == 1:
        sheet = work_book[sheet_names[0]]
        for row, object  in enumerate(data):
            for column, sub_obj in enumerate(object):
                sheet.cell(row = int(row)+1, column = int(column)+1).value = sub_obj
    work_book.save(filename = str(OUTPUT_FILE_PATH))
