import datetime
import httplib2
from googleapiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials
from modules.consts.common import SPREAD_SHEET_ID, CREDENTIALS_FILE
from modules.consts.common import WORKBOOK_HEADER_PRIVATE
from modules.consts.common import SERVICE
from modules.consts.common import HTTP_AUTH
from modules.writer import formating_data

HTTP_AUTH = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
).authorize(httplib2.Http())

SERVICE = discovery.build('sheets', 'v4', http=HTTP_AUTH)


def read_table(spreadsheetId=SPREAD_SHEET_ID, count_of_row_in_request=500):
    spreadsheet = SERVICE.spreadsheets().get(spreadsheetId=spreadsheetId).execute()
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    table = f'Расписание на {today}'
    # table = f'Расписание на 2020-03-234'
    row = 1
    info = []
    while True:
        cell_range = f'{table}!A{row}:{chr(64 + len(WORKBOOK_HEADER_PRIVATE))}{row + int(count_of_row_in_request)}'

        value = SERVICE.spreadsheets().values().get(
            spreadsheetId=spreadsheetId,
            range=cell_range,
            majorDimension='ROWS'
        ).execute()

        for row_in_responce in range(int(count_of_row_in_request) + 1):
            if len(value['values']) <= row_in_responce:
                break
            info.append({})
            for i, header in enumerate(WORKBOOK_HEADER_PRIVATE):
                print(info)
                info[-1][header] = value['values'][row_in_responce][i]
            info[-1]['row'] = row + row_in_responce
        else:
            row += int(count_of_row_in_request)
            continue
        break
    return info
