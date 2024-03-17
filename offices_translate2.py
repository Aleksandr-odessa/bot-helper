import datetime
import calendar
import os
import re
from imap_tools import MailBox, AND
from config import year, name_and_mail, mail_and_name

# import logging
from time import time

IMAP: str = os.environ['SERVER_IMAP']
MAIL_USERNAME: str = os.environ['USERNAME_MAIL']
MAIL_PASSWORD: str = os.environ['PASS_MAIL']

# file_log = logging.FileHandler("mailLog.log", "w")
# console_out = logging.StreamHandler()
# logging.basicConfig(handlers=(file_log, console_out),
#                     format='%(asctime)s, %(levelname)s, , %(message)s', datefmt='%d-%b-%y %H:%M:%S',
#                     level=logging.INFO)

class GetCountForMonth():
    def __init__(self, data: list):
        self.data = data
        self.message_list = []

    def create_list_of_data(self) -> list:
        month: int = int(self.data[0])
        day_finish: int = calendar.monthrange(year, month)[1]+1
        # creating a list of days
        list_of_days: list = [datetime.date(year, month, i) for i in range(1, day_finish)]
        return list_of_days

    def request_mail(self) -> list:
        # creating to connect to server
        with MailBox(IMAP).login(MAIL_USERNAME, MAIL_PASSWORD) as mailbox:
            # select the folder
            mailbox.folder.set('Отправленные')
            for day in self.create_list_of_data():
                for msg in mailbox.fetch(AND(date=day, text="гривен"), charset='utf-8'):
                    self.message_list.append([msg.uid, str(msg.date), msg.to, msg.text])
        return self.message_list

    @staticmethod
    def get_money(temp_list: list) -> list:
        cleared_list = []
        for mes in temp_list:
            date: str = re.search(r'\d{4}-\d{2}-\d{2}', mes[1])[0]
            split_money: str = mes[3].split('гривен')[0]
            equally: int = split_money.find('=')
            money: str = split_money[equally+2:] if equally != -1 else re.search(r'\d{2,}', split_money)[0]
            cleared_list.append([mes[0], date, mes[2][0], money])
        return cleared_list

    def request_summ(self) -> str:
        start_time = time()
        list_message: list = self.request_mail()
        messages: list = self.get_money(list_message)
        get_email: list = [_[2] for _ in messages]
        dict_of_messengers = {}
        for email in get_email:
            temp: list = [int(mes[3]) for mes in messages if email in mes]
            string: str = "  ".join(["суммы:", str(temp), "общая сумма", str(sum(temp))])
            dict_of_messengers[mail_and_name.get(email)] = string
        finish_time = time()
        res_time = finish_time - start_time
        print(res_time)
        return str(dict_of_messengers)



class GetCountForPeriod(GetCountForMonth):

    def start_month_day(self) -> tuple:
        day_month: list = self.data.split(".")
        return int(day_month[0]), int(day_month[1])