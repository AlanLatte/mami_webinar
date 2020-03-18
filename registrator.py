from common import HEADERS as headers

def register_to_vebinar(eventsessionID, name, email):
    url     = f'https://userapi.webinar.ru/v3/eventsessions/{str(eventsessionID)}/register'
    names = name_refactor(name)
    emails = email_refactoring(email)
    for id in range(len(names)):
        body    =   {
                        'name'  :   str(names[id]),
                        'role'  :   'LECTURER',
                        'email' :   str(emails[id]),
                    }
        print(requests.post(url, data=body, headers=headers).json())

def name_refactor(name):
    name = name.split('|')
    return name

def email_refactoring(email):
    email = name.split('|')
    return email