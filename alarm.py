from datetime import datetime
def alarm(time):

    time = time.split(':') #splits hours and minutes
    
    wake_up_time = map(int, time) #converts str to int
    
    wake_up_time =list(wake_up_time) #converted into list
    
    wake_up_hour = wake_up_time[0] 
    
    wake_up_minute = wake_up_time[1]

    now = datetime.now().time()  #gets current time
    
    current_hour, current_minute =now.hour, now.minute

    hours_remaining = (wake_up_hour-current_hour) % 24,
    hours_remaining = hours_remaining[0]
    
    minutes_remaining = (wake_up_minute-current_minute)

    if minutes_remaining < 0:
        hours_remaining = hours_remaining - 1
        minutes_remaining = minutes_remaining % 60
    else:
        minutes_remaining = minutes_remaining % 60
        
    print("I will have been sleeping for", hours_remaining, "hours and",minutes_remaining, "minutes")
