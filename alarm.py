from datetime import datetime
def alarm(time):

    time = time.split(':')
    
    wake_up_time = map(int, time)
    
    wake_up_time =list(wake_up_time)
    
    wake_up_hour = wake_up_time[0]
    
    wake_up_minute = wake_up_time[1]
    
    wake_up_second = 0

    now = datetime.now().time()
    
    current_hour, current_minute, current_second =now.hour, now.minute, now.second

    hours_remaining = (wake_up_hour-current_hour) % 24,
    hours_remaining = hours_remaining[0]
    
    minutes_remaining = (wake_up_minute-current_minute)

    if minutes_remaining < 0:
        hours_remaining = hours_remaining - 1
        minutes_remaining = minutes_remaining % 60
    else:
        minutes_remaining = minutes_remaining % 60
        
    print("I will have been sleeping for", hours_remaining, "hours and",minutes_remaining, "minutes")
