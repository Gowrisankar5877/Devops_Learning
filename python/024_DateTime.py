# import datetime 
# print(dir(datetime))
from datetime import datetime
import pytz
now = datetime(2025,5,1,10,20,5)
now.strftime("%m/%d/%Y, %H:%M:%S")
now =datetime.now(pytz.timezone('US/Eastern'))
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
print(now,day,month,year,hour, minute, second)