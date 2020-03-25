import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from modules.writer import formating_data
from modules.google_table.checker import check_name
from modules.consts.common import SPREAD_SHEET_ID
from modules.consts.common import CREDENTIALS_FILE,
from modules.consts.common import HTTP_AUTH
from modules.consts.common import SERVICE



spreadsheet = SERVICE.spreadsheets().get(
    spreadsheetId = SPREAD_SHEET_ID
).execute()


def create_virtual_table(title='Сие есть название документа2'):
    spreadsheet = SERVICE.spreadsheets().create(
        body = {
            'properties': {
                'title': title, 'locale': 'ru_RU'
                },
        # 'sheets': [{'properties': {'sheetType': 'GRID',
        #                            'sheetId': 0,
        #                            'title': 'Сие есть название листа',
        #                            'gridProperties': {'rowCount': 8, 'columnCount': 5}}}]
        }
    ).execute()

    print(spreadsheet)

    driveService = apiclient.discovery.build('drive', 'v3', http = HTTP_AUTH)
    shareRes = driveService.permissions().create(
        fileId=spreadsheet['spreadsheetId'],
        body={
            'type': 'anyone',
            'role': 'writer'
        },  # доступ на чтение кому угодно
        fields='id'
    ).execute()
    print(f"{str(spreadsheet['spreadsheetUrl'])}")
    print(spreadsheet['spreadsheetId'])


def create_new_sheet(info: list, spreadsheetID: str=SPREAD_SHEET_ID,):
    request_body, sheet_name = prepair_data(info)
    spreadsheet = SERVICE.spreadsheets().get(spreadsheetId=spreadsheetID).execute()

    append_list = SERVICE.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet['spreadsheetId'],
        body={
            "requests": [{
                "addSheet": {
                    'properties': {
                            'sheetType': 'GRID',
                            'sheetId': get_free_sheet_id(spreadsheet),
                            'title': check_name(sheet_name=sheet_name, spreadsheet=spreadsheet)# sheet_name,
                        }
                    }
                }
            ],
            "includeSpreadsheetInResponse": False,
            "responseIncludeGridData": True
        }
    ).execute()

    append_info = SERVICE.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheetID, body={
            "valueInputOption": "USER_ENTERED",
            "data": request_body
        }
    ).execute()

def prepair_data(info: list):
    for row in info:
        values = formating_data(info, {'type':'private'})
        for value in values:
            value.append('inactive')
        sheet_name = f"Расписание на {values[0][0]}"

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

# results = SERVICE.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheet['spreadsheetId'], body = {
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
    # id = create_virtual_table(SERVICE)
    print('id')
    # create_new_sheet(id)
