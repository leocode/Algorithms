import datetime
import re
def alarm(alarm_time):
    if not re.match("^\d\d:\d\d$", alarm_time):
        raise ValueError("Provided date string is not supported. Valid time string: HH:MM")
    hour, minute = int(alarm_time.split(":")[0]), int(alarm_time.split(":")[1])
    now = datetime.datetime.now()
    alarm_day = datetime.date.today() + datetime.timedelta(days=1) if hour <= now.hour else datetime.date.today()
    alarm_time = datetime.datetime(year=alarm_day.year, month=alarm_day.month,
                                   day=alarm_day.day, hour=hour, minute=minute)
    delta_t = max((now, alarm_time)) - min((now, alarm_time))
    hours = int(delta_t.seconds / 3600)
    minutes = int((delta_t.seconds % 3600) / 60)
    print(f"You will be sleeping for {hours} hours and {minutes} minutes.")