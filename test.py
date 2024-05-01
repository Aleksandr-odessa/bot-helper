from offices_translate2 import GetCountForMonth, GetCountForPeriod
from offices_translate import request_summ
import time
import datetime

one_month = GetCountForMonth('2')
# day_month = GetCountForPeriod('01.15')

jan = one_month.create_list_of_days()
# # test_jan = request_summ('1')
# # assert len(jan) == 52
# print(f'jan={jan}')
# print(len(jan))
# # print(f'test_jan={test_jan}')
# january15 =
print(jan)