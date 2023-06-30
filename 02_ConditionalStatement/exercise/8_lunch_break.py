from math import ceil

name_series = str(input())
episode_duration = int(input())
break_duration = int(input())

time_for_lunch = break_duration / 8
leisure_time = break_duration / 4

time_taken = episode_duration + time_for_lunch + leisure_time
time_left = break_duration - time_taken

if time_left >= 0:
    print(f"You have enough time to watch {name_series} and left with {ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_series}, you need {ceil(abs(time_left))} more minutes.")