from datetime import datetime

def alarm(time_alarm):
    a_hour = int(time_alarm.split(':')[0])
    a_min = int(time_alarm.split(':')[1])
    n_hour = datetime.now().hour
    n_min = datetime.now().minute
    
    if a_hour < n_hour:
        a_hour += 24
    elif a_hour == n_hour and a_min < n_min:
        a_hour += 24
    if a_min < n_min:
        a_min += 60
        a_hour -= 1

    print("I will have been sleeping for %d hour(s) and %d minute(s)."%(a_hour-n_hour, a_min-n_min))

# if now is 22:55
print("Alarm 5:30")
alarm("5:30")
# I will have been sleeping for 6 hour(s) and 35 minute(s).
print("Alarm 22:30")
alarm("22:30")
# I will have been sleeping for 23 hour(s) and 35 minute(s).
print("Alarm 23:00")
alarm("23:00")
# I will have been sleeping for 0 hour(s) and 5 minute(s).
