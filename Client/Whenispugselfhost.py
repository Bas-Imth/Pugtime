import datetime
import time
wanted_day = 'saturday'
wanted_time = 19

list = [['monday', 0],['tuesday', 1],['wednesday', 2],['thursday', 3],['friday', 4],['saturday', 5],['sunday', 6]]

for i in list:
    if wanted_day == i[0]:
        number_wanted_day = i[1]

today = datetime.datetime.today().weekday()
days = number_wanted_day
time = time.localtime(time.time() + time.timezone)

if wanted_time > time[3]:
    hours = wanted_time - time[3] - 1
    mins = 59 - time[4]
    secs = 59 - time[5]

else:
    days = days
    hours = 23 - time[3] + wanted_time #- 1 #Not sure if one hour off or not.
    mins = 59 - time[4]
    secs = 59 - time[5]

print("%d day(s), %d hour(s), %d minute(s) and %d second(s) left untill the next PUG!" % (days, hours, mins, secs))
input("Press Enter to continue...")
