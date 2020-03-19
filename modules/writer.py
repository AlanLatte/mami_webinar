from openpyxl import load_workbook
from openpyxl import Workbook

def write_data(sheet_, wb, event_session_id, link, room, row, file):
    sheet_.cell(row = row, column = 9).value = link
    sheet_.cell(row = row, column = 10).value = room
    sheet_.cell(row = row, column = 15).value = event_session_id
    wb.save(file)


def merge_workbook(data: list, name: str):
    wb = Workbook()
    sheet = wb['Worksheet']
    for row, object  in enumerate(data):
        for column, sub_obj in enumerate(object):
            sheet_cell(row = row, column = column).value = sub_obj
    wb.save(filename = str(name))
