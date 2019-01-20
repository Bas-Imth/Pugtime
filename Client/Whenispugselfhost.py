import datetime
import time
wanted_day = 'saturday'
wanted_time = 21

list = [['monday', 0],['tuesday', 1],['wednesday', 2],['thursday', 3],['friday', 4],['saturday', 5],['sunday', 6]]

for i in list:
    if wanted_day == i[0]:
        number_wanted_day = i[1]

today = datetime.datetime.today().weekday()
days = number_wanted_day 
time = time.localtime(time.time() + time.timezone)

if wanted_time > time[3]:
    hours = wanted_time - time[3]
    mins = 59 - time[4]
    secs = 59 - time[5]

else:
    days = days - 1
    hours = 23 - time[3] + wanted_time
    mins = 59 - time[4]
    secs = 59 - time[5]

print( [days, 'day(s)', hours,'hour(s)', mins,'minute(s) and', secs,'seconds untill the Saturday PUG!'])