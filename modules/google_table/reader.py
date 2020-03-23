import datetime
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from modules.consts.common import SPREAD_SHEET_ID
from modules.consts.common import WORKBOOK_HEADER_PRIVATE
from modules.writer import formating_data

from modules.consts.common import SPREAD_SHEET_ID, CREDENTIALS_FILE


httpAuth = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
).authorize(httplib2.Http())

service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

# spreadsheet = service.spreadsheets().get(spreadsheetId = '1e_DqDCwrc3xlTWsXDB-zUuchWSWH_HA6wzogKbXPStE').execute()


def read_cells(spreadsheetId=SPREAD_SHEET_ID):
    spreadsheet = service.spreadsheets().get(spreadsheetId = spreadsheetId).execute()
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    # table = f'Расписание на {today}' + '4'
    table = 'Расписание на 2020-03-234'
    row = 1
    info = []
    while True:
        cell_range = f'{table}!A{row}:{chr(64+len(WORKBOOK_HEADER_PRIVATE))}{row+100}'

        value = service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId,
            range=cell_range
        ).execute()

        info.append({})
        for row_id in range(101):
            for i, header in enumerate(WORKBOOK_HEADER_PRIVATE):
                if value['values'][row_id][i] == '':
                    break
                info[-1][header] = value['values'][row_id][i]
            else:
                continue
            break

    return info

# def get_counts_of_row(spreadsheetId='1e_DqDCwrc3xlTWsXDB-zUuchWSWH_HA6wzogKbXPStE'):
#     spreadsheet = service.spreadsheets().get(spreadsheetId = spreadsheetId).execute()
#     cell_range = f'{table}!A{row}:{chr(64+len(WORKBOOK_HEADER_PRIVATE))}{row}'
