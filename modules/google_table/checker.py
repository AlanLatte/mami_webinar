import re


def check_name(sheet_name, spreadsheet=None):
    sheets = spreadsheet.get("sheets", "")
    counter_sheets_regexp = re.compile(pattern=r"\((\d)+\)+$")
    if sheet_name in [a["properties"]["title"] for a in sheets]:
        counter_information = sum(
            [
                [
                    (string, int(finder.group()[1:-1]), finder.span(),)
                    for finder in counter_sheets_regexp.finditer(string)
                ]
                for string in [sheet for sheet in sheets if sheet_name in sheet]
                if counter_sheets_regexp.search(string)
            ],
            [],
        )

        if counter_information:
            counter_information = max(counter_information)
            return counter_information[0].replace(
                counter_information[0][
                    counter_information[-1][0] : counter_information[-1][1]
                ],
                f"({str(counter_information[1]+1)})",
            )
        else:
            return f"{sheet_name}(1)"
    else:
        return sheet_name
