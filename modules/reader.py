from modules.time_manager import converter_time
from openpyxl import load_workbook
from .consts.common import INPUT_DIR_PATH
import os

directory = '../input'


def read_row_from_exel(sheet_, row):
    # output_data = converter_time(sheet_.cell(row = row, column = 1).value)              #year, month, day
    output_data = [2020, 3]
    output_data.append(sheet_.cell(row = row, column = 1).value)                        #дата
    output_data.append(sheet_.cell(row = row, column = 3).value)                        #name
    output_data.append(sheet_.cell(row = row, column = 4).value)                        #email
    output_data.append(sheet_.cell(row = row, column = 6).value)                        #subject
    output_data.append(str(sheet_.cell(row=row, column = 7).value))                        #start_t
    return output_data

def full_read_exel_file(path):
    book_data = []
    row = 2
    while True:
        wb      = load_workbook(path, data_only=True)
        sheet_  = wb['Worksheet']
        book_data.append(read_row_from_exel(sheet_, row))
        row += 1
        if sheet_.cell(row = row, column = 1).value == None:
            break
    return book_data

def read_all_info():
    all_data = []
    files = os.listdir(INPUT_DIR_PATH)
    exel_files = filter(lambda x: x.endswith('.xlsx'), files)
    for file in exel_files:
        all_data = [*all_data, *full_read_exel_file(INPUT_DIR_PATH+f'/{file}')]
    return all_data
