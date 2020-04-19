import smtplib  # Импортируем библиотеку по работе с SMTP
import os  # Функции для работы с операционной системой, не зависящие от используемой операционной системы

from modules.consts.common import OUTPUT_DIR_PATH

import mimetypes  # Импорт класса для обработки неизвестных MIME-типов, базирующихся на расширении файла
from email import encoders  # Импортируем энкодер
from email.mime.base import MIMEBase  # Общий тип
from email.mime.text import MIMEText  # Текст/HTML
from email.mime.image import MIMEImage  # Изображения
from email.mime.audio import MIMEAudio  # Аудио
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект


def send_all(file_to_email):
    for file, email in file_to_email.items():
        send_email(
            addr_to=email,
            msg_subj="Расписание вебинаров",
            msg_text="",
            files=[os.path.join(OUTPUT_DIR_PATH, file)],
        )
    send_email(
        addr_to="a.s.zhuplev@mospolytech.ru",
        msg_subj="Расписание вебинаров",
        msg_text="",
        files=[os.path.join(OUTPUT_DIR_PATH)],
    )


def send_email(addr_to, msg_subj, msg_text, files):
    addr_from = "4.leo.makarov@gmail.com"  # Отправитель
    password = "venfzdniijabquja"  # Пароль

    msg = MIMEMultipart()  # Создаем сообщение
    msg["From"] = addr_from  # Адресат
    msg["To"] = addr_to  # Получатель
    msg["Subject"] = msg_subj  # Тема сообщения

    body = msg_text  # Текст сообщения
    msg.attach(MIMEText(body, "plain"))  # Добавляем в сообщение текст

    process_attachement(msg, files)

    # ======== Этот блок настраивается для каждого почтового провайдера отдельно ======================================
    server = smtplib.SMTP("smtp.gmail.com", 587)  # Создаем объект SMTP
    server.starttls()  # Начинаем шифрованный обмен по TLS
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()
    # ================================================================================================================


def process_attachement(msg, files):
    for f in files:
        if os.path.isfile(f):  # Если файл существует
            attach_file(msg, f)  # Добавляем файл к сообщению
        elif os.path.exists(f):  # Если путь не файл и существует, значит - папка
            dir = os.listdir(f)  # Получаем список файлов в папке
            for file in dir:  # Перебираем все файлы и...
                attach_file(
                    msg, os.path.join(f, file)
                )  # ...добавляем каждый файл к сообщению


def attach_file(msg, filepath):  # Функция по добавлению конкретного файла к сообщению
    filename = os.path.basename(filepath)  # Получаем имя файла
    ctype, encoding = mimetypes.guess_type(
        filepath
    )  # Определяем тип файла на основе его расширения
    if ctype is None or encoding is not None:  # Если тип файла не определяется
        ctype = "application/octet-stream"  # Будем использовать общий тип
    maintype, subtype = ctype.split("/", 1)  # Получаем тип и подтип
    if maintype == "text":  # Если текстовый файл
        with open(filepath) as fp:  # Открываем файл для чтения
            file = MIMEText(fp.read(), _subtype=subtype)  # Используем тип MIMEText
            fp.close()
    else:  # Неизвестный тип файла
        with open(filepath, "rb") as fp:
            file = MIMEBase(maintype, subtype)  # Используем общий MIME-тип
            file.set_payload(
                fp.read()
            )  # Добавляем содержимое общего типа (полезную нагрузку)
            encoders.encode_base64(file)  # Содержимое должно кодироваться как Base64
    file.add_header(
        "Content-Disposition", "attachment", filename=filename
    )  # Добавляем заголовки
    msg.attach(file)  # Присоединяем файл к сообщению
