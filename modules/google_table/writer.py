import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from modules.writer import formating_data
from modules.consts.common import SPREAD_SHEET_ID


CREDENTIALS_FILE = r'C:\Users\leo\Desktop\snappy-topic-271911-62bc34f9811c.json'  # имя файла с закрытым ключом

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
)

httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

spreadsheet = service.spreadsheets().get(
    spreadsheetId = SPREAD_SHEET_ID
).execute()


def create_virtual_table(service):
    spreadsheet = service.spreadsheets().create(
        body = {
            'properties': {
                'title': 'Сие есть название документа1', 'locale': 'ru_RU'
                },
        # 'sheets': [{'properties': {'sheetType': 'GRID',
        #                            'sheetId': 0,
        #                            'title': 'Сие есть название листа',
        #                            'gridProperties': {'rowCount': 8, 'columnCount': 5}}}]
        }
    ).execute()

    print(spreadsheet)

    driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth)
    shareRes = driveService.permissions().create(
        fileId=spreadsheet['spreadsheetId'],
        body={
            'type': 'anyone',
            'role': 'reader'
        },  # доступ на чтение кому угодно
        fields='id'
    ).execute()
    print(f"{str(spreadsheet['spreadsheetUrl'])}")
    return spreadsheet['spreadsheetId']


def create_new_sheet(info: list, spreadsheetID: str=SPREAD_SHEET_ID,):
    request_body, sheet_name = prepair_data(info)
    spreadsheet = service.spreadsheets().get(spreadsheetId=preadsheetID).execute()
    append_list = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet['spreadsheetId'],
        body={
            "requests": [{
                "addSheet": {
                    'properties': {
                            'sheetType': 'GRID',
                            'sheetId': get_free_sheet_id(spreadsheet),
                            'title': sheet_name,
                        }
                    }
                }
            ],
            "includeSpreadsheetInResponse": False,
            "responseIncludeGridData": True
        }
    ).execute()

    print(request_body)
    append_info = service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheetID, body={
            "valueInputOption": "USER_ENTERED",
            "data": request_body
        }
    ).execute()

def prepair_data(info: list):
    for row in info:
        values = formating_data(info, {'type':'private'})
        sheet_name = f"Расписание на {values[0][0]}"+'4'

    request = {
        "range": f"{sheet_name}!A1:{chr(64+len(values[0]))}{len(values)}",
        "majorDimension": "ROWS",
        "values": values
    }
    return request, sheet_name

def get_free_sheet_id(spreadsheet):
    mass = [
        i['properties']['sheetId'] for i in spreadsheet['sheets']
    ]
    return(max(mass)+1)

# results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheet['spreadsheetId'], body = {
#     "valueInputOption": "USER_ENTERED",
#     "data": [
#         {"range": "Сие есть название листа!B2:C3",
#          "majorDimension": "ROWS",     # сначала заполнять ряды, затем столбцы (т.е. самые внутренние списки в values - это ряды)
#          "values": [["This is B2", "This is C2"], ["This is B3", "This is C3"]]},
#
#         {"range": "Сие есть название листа!D5:E6",
#          "majorDimension": "COLUMNS",  # сначала заполнять столбцы, затем ряды (т.е. самые внутренние списки в values - это столбцы)
#          "values": [["This is DOOMER", "This is D6"], ["This is E5", "=5+5"]]}
#     ]
# }).execute()

if __name__ == '__main__':
    # id = create_virtual_table(service)
    print('id')
    # create_new_sheet(id)
