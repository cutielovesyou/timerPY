from time import sleep
import os
second=0
minute=0
hour=0
day=0
while True:
    os.system('cls'if os.name=='nt'else'clear')
    print(f'Day: {day}\nHour: {hour}\nMinute: {minute}\nSecond: {second}')
    second=second+1
    if second==60:
        minute=minute+1
        second=0
    if minute==60:
        hour=hour+1
        minute=0
    if hour==24:
        day=day+1
        hour=0
    sleep(1)
