import datetime
import calendar
from imap_tools import MailBox, AND
from config import mail_and_name, pass_mail, username_mail, server_imap, name_and_mail, year
import re
import logging
from time import time

IMAP: str = server_imap
USERNAME: str = username_mail
MAIL_PASSWORD: str = pass_mail

list_data = []
# file_log = logging.FileHandler("mailLog.log", "w")
# console_out = logging.StreamHandler()
# logging.basicConfig(handlers=(file_log, console_out),
#                     format='%(asctime)s, %(levelname)s, , %(message)s', datefmt='%d-%b-%y %H:%M:%S',
#                     level=logging.INFO)


def select_month_day(data: str) -> tuple:
    if data.isalnum():
        month: int = int(data)
        day_start: int = 1
    else:
        day_month: list = data.split(".")
        month: int = int(day_month[1])
        day_start: int = int(day_month[0])
    return day_start, month


def request_mail(data: list) -> list:

    # data = [translate office, date]
    message_list = []
    month_day: tuple = select_month_day(data[0])
    month: int = month_day[1]
    day_start: int = month_day[0]
    day_finish: tuple = calendar.monthrange(year, month)
    # creating a list of days
    list_of_days: list = [datetime.date(year, month, i) for i in range(day_start, day_finish[1] + 1)]
    len_data: int = len(data)
    # creating to connect to server
    start_time = time()
    with MailBox(server_imap).login(username_mail, pass_mail) as mailbox:
        # select the folder
        mailbox.folder.set('Отправленные')
        if len_data >= 2:
            mail = name_and_mail.get(data[1])
            for day in list_of_days:
                for msg in mailbox.fetch(AND(date=day, to=mail)):
                    message_list.append([msg.uid, str(msg.date), msg.to, msg.text])
        else:
            for day in list_of_days:
                for msg in mailbox.fetch(AND(date=day)):
                    message_list.append([msg.uid, str(msg.date), msg.to, msg.text])
    end_time = time()
    res_time = end_time-start_time
    print(f'res_time={res_time}')
    return message_list


def request_mail2(list_of_days: list, data:list) -> list:
    len_data: int = len(data)
    start_time = time()
    if len_data < 2:
        with MailBox(server_imap).login(username_mail, pass_mail) as mailbox:
            # select the folder
            mailbox.folder.set('Отправленные')
            for day in list_of_days:
                message_list: list = [[msg.uid, str(msg.date), msg.to, msg.text] for msg in mailbox.fetch(AND(date=day))]
    else:
        mail = name_and_mail.get(data[1])
        with MailBox(server_imap).login(username_mail, pass_mail) as mailbox:
        # select the folder
            mailbox.folder.set('Отправленные')
            for day in list_of_days:
                message_list: list = [[msg.uid, str(msg.date), msg.to, msg.text] for msg in mailbox.fetch(AND(date=day, to=mail))]
    end_time = time()
    res_time = end_time - start_time
    print(f'res_time2={res_time}')
    return message_list

def create_list_of_days(data:list) -> list:
    month_day: tuple = select_month_day(data[0])
    month: int = month_day[1]
    day_finish: tuple = calendar.monthrange(year, month)
    # creating a list of days
    list_of_days: list = [datetime.date(year, month, i) for i in range(month_day[0], day_finish[1] + 1)]
    return list_of_days


def get_money(list_message: list) -> list:
    find_word: str = "гривен"
    cleared_list = []
    temp_list = [mes for mes in list_message if find_word in mes[3]]
    for mes in temp_list:
        date: str = re.search(r'\d{4}-\d{2}-\d{2}', mes[1])[0]
        money: str = mes[3].split('гривен')[0]
        equally: int = money.find('=')
        money: str = money[equally+2:] if equally != -1 else re.search(r'\d{2,}', money)[0]
        cleared_list.append([mes[0], date, mes[2][0], money])
    return cleared_list


def request_summ(data) -> str:
    list_message: list = request_mail(data)
    messages: list = get_money(list_message)
    set_email: list = [i[2] for i in messages]
    dict_of_messengers = {}
    for email in set_email:
        temp: list = [int(mes[3]) for mes in messages if email in mes]
        string: str = "  ".join(["суммы:", str(temp), "общая сумма", str(sum(temp))])
        dict_of_messengers[mail_and_name.get(email)] = string
    return str(dict_of_messengers)


def check_data(data: str) -> bool:
    return bool(re.fullmatch(r'\d{1,2}\.\d{1,2}', data))

