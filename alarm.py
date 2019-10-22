from datetime import datetime, timedelta, time

hour,minutes = '6:30'.split(':')
print(hour, minutes)

actual_time = datetime.combine(datetime.now().time()
wake_time = time(int(hour),int(minutes),00)

print(type(wake_time), type(actual_time))
sleep_time = wake_time - actual_time
print(sleep_time)


# wake_time = (hour)
# print(actual_date)