#--date time

import time

print(time.time())

print('Local time: ')
print(time.localtime())

print(time.localtime(time.time()))

format_time=time.asctime(time.localtime(time.time()))
print('Format time :',format_time)


import calendar

print(calendar.month(2025,6))

