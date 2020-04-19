import datetime
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from modules.consts.common import SPREAD_SHEET_ID
from modules.consts.common import CREDENTIALS_FILE
from modules.consts.common import WORKBOOK_HEADER_PRIVATE
from modules.consts.common import HTTP_AUTH
from modules.consts.common import SERVICE


HTTP_AUTH = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
).authorize(httplib2.Http())

SERVICE = apiclient.discovery.build('sheets', 'v4', http = HTTP_AUTH)

def update_status(row, \
    sheet_name=f'Расписание на {datetime.datetime.now().strftime("%Y-%m-%d")}',\
                                                            status='inactive'):
    spreadsheet = SERVICE.spreadsheets().get(spreadsheetId=SPREAD_SHEET_ID).execute()
    append_info = SERVICE.spreadsheets().values().batchUpdate(
        spreadsheetId=SPREAD_SHEET_ID, body={
            "valueInputOption": "USER_ENTERED",
            "data": {
                "range": f"{sheet_name}!{chr(64+WORKBOOK_HEADER_PRIVATE.index('status')+1)}{str(row)}",
                "majorDimension": "ROWS",
                "values": [[status]]
            }
        }
    ).execute()
