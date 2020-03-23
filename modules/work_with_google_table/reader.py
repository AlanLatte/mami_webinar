import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from modules.writer import formating_data
import datetime

from modules.consts.common import WORKBOOK_HEADER_PRIVATE as header_privaye


CREDENTIALS_FILE = r'C:\Users\leo\Desktop\snappy-topic-271911-62bc34f9811c.json'  # имя файла с закрытым ключом

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
                                                                                  'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

# spreadsheet = service.spreadsheets().get(spreadsheetId = '1e_DqDCwrc3xlTWsXDB-zUuchWSWH_HA6wzogKbXPStE').execute()


def read_from_excel_table(spreadsheetId='1e_DqDCwrc3xlTWsXDB-zUuchWSWH_HA6wzogKbXPStE'):
    spreadsheet = service.spreadsheets().get(spreadsheetId = spreadsheetId).execute()
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    # table = f'Расписание на {today}' + '4'
    table = 'Расписание на 2020-03-234'
    row = 1
    info = []
    while True:
        range_ = f'{table}!A{row}:{chr(64+len(header_privaye))}{row+100}'
        value = service.spreadsheets().values().get(spreadsheetId = spreadsheetId, range=range_).execute()
        info.append({})

        for row_id in range(101):
            for i, header in enumerate(header_privaye):
                if value['values'][row_id][i] == '':
                    break
                info[-1][header] = value['values'][row_id][i]
            else:
                continue
            break


    return info

# def get_counts_of_row(spreadsheetId='1e_DqDCwrc3xlTWsXDB-zUuchWSWH_HA6wzogKbXPStE'):
#     spreadsheet = service.spreadsheets().get(spreadsheetId = spreadsheetId).execute()
#     range_ = f'{table}!A{row}:{chr(64+len(header_privaye))}{row}'
