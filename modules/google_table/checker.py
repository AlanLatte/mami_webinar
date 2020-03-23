import re

def check_name(sheet_name: str, spreadsheet=None):
    sheets = spreadsheet.get('sheets', '')
    counter_sheets_regexp = re.compile(pattern=r"\((\d)+\)+$")
    if sheet_name in [
        sheet['properties']['title'] for sheet in sheets
    ]:
        start_position, end_position = [
            a.span() for a in counter_sheets_regexp.finditer(string=sheet_name)
        ][0]
        counter_sheets_number = [
            a.group()[1:-1] for a in counter_sheets_regexp.finditer(string=sheet_name)
        ][0]

        if counter_sheets_regexp:
            return sheet_name.replace(
                sheet_name[
                    start_position:end_position
                ],
                f"({int(counter_sheets_number)+1})"
            )
        else:
            return f"{sheet_name}(1)"
