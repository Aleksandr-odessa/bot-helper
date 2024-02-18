from offices_translate import request_mail2, request_mail, create_list_of_days
import time

days = create_list_of_days(["1"])
start_time = time.time()
mail: list = request_mail(["1"])
end_time = time.time()
result_time = end_time-start_time
# print (mail)
print(result_time)
start_time2 = time.time()
# test_list = [day for day in range(173126, 174167)]
mail2: list = request_mail2(days,["1"])
end_time2 = time.time()
result_time2 = end_time2-start_time2
# # print (mail2)
print(result_time2)