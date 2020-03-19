from modules.time_manager import converter_time
from openpyxl import load_workbook
from .consts.common import INPUT_DIR_PATH
import os


def read_row_from_exel(sheet, row):
    CELLS = {
        "name": sheet.cell(row=row, column=3).value,
        "email": sheet.cell(row=row, column=4).value,
        "subject": sheet.cell(row=row, column=6).value,
        "start_t": str(sheet.cell(row=row, column=7).value),
        "id": str(sheet.cell(row=row, column=2).value),
    }
    output_data = []
    time = converter_time(sheet.cell(row=row, column=1).value)
    output_data.extend([int(t) for t in time])
    output_data.append(CELLS["name"])
    output_data.append(CELLS["email"])
    output_data.append(CELLS["subject"])
    output_data.append(CELLS["start_t"])
    output_data.append(CELLS["id"])
    return output_data


def full_read_exel_file(path):
    book_data = []
    row = 2
    while True:
        wb = load_workbook(path, data_only=True)
        sheet = wb['Worksheet']
        book_data.append(read_row_from_exel(sheet, row))
        row += 1
        if sheet.cell(row=row, column=1).value is None:
            break
    return book_data


def read_all_info():
    all_data = []
    files = os.listdir(INPUT_DIR_PATH)
    exel_files = filter(lambda x: x.endswith('.xlsx'), files)
    for file in exel_files:
        all_data = [*all_data, *full_read_exel_file(INPUT_DIR_PATH+f'/{file}')]
    return all_data
