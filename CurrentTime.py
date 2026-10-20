
import time
currentTime=time.time()
totalSeconds=int(currentTime)
# get current second
currentSecond=totalSeconds % 60
# get current minute
totalMinutes=totalSeconds // 60
currentMinute=totalMinutes % 60
# get current hour
totalHours=totalMinutes // 60
currentHour=totalHours % 24
# for ugandan time(EAT is GMT+3)
currentHour=(currentHour + 3) % 24
# display
print("current time is",currentHour,":",currentMinute,":",currentSecond,"EAT")