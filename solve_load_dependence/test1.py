
import time

""" 
https://stackoverflow.com/questions/36590963/is-this-a-reliable-countdown-timer
"""


# store the current time
start_time = time.time() 
print(start_time)


hours = 0
minutes = 0
seconds = 10

# target_time = start_time + (hr * 60 + min) * 60 + sec


start_time = time.time() 
target_time = start_time + (hours * 60 + minutes) * 60 + seconds

while target_time > time.time():

    # do something, e.g. print the remaining time:
    remaining_time = target_time - time.time()
    print(f'Countdown: {remaining_time // 3600} h {remaining_time // 60} min {remaining_time % 60}s remaining')

    # sleep a bit to save CPU resources
    time.sleep(0.5)