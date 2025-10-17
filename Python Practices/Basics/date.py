from datetime import date,timedelta
from datetime import datetime


cur_date=date.today()
print('Current date :',cur_date)


cur_time=datetime.now()
print('Current date time :',cur_time)

format_date=cur_time.strftime('%y-%m-%d') #--string format time
print(format_date)

cur_date=date.today()

a=cur_date+timedelta(days=1)
b=cur_date-timedelta(days=1)

print('Incremented date :',a)
print('Decremented date :',b)

