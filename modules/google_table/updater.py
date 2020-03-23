import datetime
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from modules.consts.common import SPREAD_SHEET_ID, CREDENTIALS_FILE
from modules.consts.common import WORKBOOK_HEADER_PRIVATE


httpAuth = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
).authorize(httplib2.Http())

service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

def update_status(row, \
    sheet_name=f'Расписание на {datetime.datetime.now().strftime("%Y-%m-%d")}',\
                                                            status='inactive'):
    spreadsheet = service.spreadsheets().get(spreadsheetId=SPREAD_SHEET_ID).execute()
    append_info = service.spreadsheets().values().batchUpdate(
        spreadsheetId=SPREAD_SHEET_ID, body={
            "valueInputOption": "USER_ENTERED",
            "data": {
                "range": f"{sheet_name}!{chr(64+WORKBOOK_HEADER_PRIVATE.index('status')+1)}{str(row)}",
                "majorDimension": "ROWS",
                "values": [[status]]
            }
        }
    ).execute()
