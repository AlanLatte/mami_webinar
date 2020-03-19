import openpyxl

# def write_data(sheet_, wb, event_session_id, link, room, row, path):
#     sheet_.cell(row = row, column = 9).value = link
#     sheet_.cell(row = row, column = 10).value = room
#     sheet_.cell(row = row, column = 15).value = event_session_id
#     wb.save(path)


def write_data(data: lits):
    for row, object  in enumerate(data):
        for column, sub_obj in enumerate(object):
            sheet_.cell(row = row, column=column).value = sub_obj
