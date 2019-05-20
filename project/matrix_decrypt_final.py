# Matrix Encryption
# by: The Epidemics

from sys import stdin
from math import log, floor, ceil

def swap(plaintext, shift, ITERATIONS):
    plaintext = list(plaintext)
    num_loops = floor(len(plaintext) / ITERATIONS)
    inc = int(ITERATIONS/9)
    for i in shift:
        j = 0
        while j < num_loops:
            temp = plaintext[(j*ITERATIONS)+(4*inc):(j*ITERATIONS)+(4*inc)+inc]
            plaintext[(j*ITERATIONS)+(4*inc):(j*ITERATIONS)+(4*inc)+inc] = plaintext[(j*ITERATIONS)+(i*inc):(j*ITERATIONS)+(i*inc)+inc]
            plaintext[(j*ITERATIONS)+(i*inc):(j*ITERATIONS)+(i*inc)+inc] = temp
            j += 1
    return plaintext

def pad(plaintext):
    padding = "#"
    n = len(plaintext)%9
    if n != 0:
        num_pad = 9 - n
        while(num_pad > 0):
            plaintext = plaintext + padding
            num_pad -= 1
    return plaintext

def shift_calc(time):
    time = time.split(":")
    hour = int(time[0])
    minute = int(time[1])
    second =  int(time[2])
    shift = []

    # Second Shift
    if second >= 5 and second <= 10:
        shift.append(2)
    elif second >= 11 and second <= 19:
        shift.append(5)
    elif second >= 20 and second <= 25:
        shift.append(8)
    elif second >= 26 and second <= 34:
        shift.append(7)
    elif second >= 35 and second <= 40:
        shift.append(6)
    elif second >= 41 and second <= 49:
        shift.append(3)
    elif second >= 50 and second <= 55:
        shift.append(0)
    elif (second >= 56 and second <= 59) or (second >= 0 and second <= 4):
        shift.append(1)
    else:
        return -1

    # Minute Shift
    if 5 <= minute <= 10:
        shift.append(2)
    elif 11 <= minute <= 19:
        shift.append(5)
    elif 20 <= minute <= 25:
        shift.append(8)
    elif minute >= 26 and minute <= 34:
        shift.append(7)
    elif minute >= 35 and minute <= 40:
        shift.append(6)
    elif minute >= 41 and minute <= 49:
        shift.append(3)
    elif minute >= 50 and minute <= 55:
        shift.append(0)
    elif (minute >= 56 and minute <= 59) or (minute >= 0 and minute <= 4):
        shift.append(1)
    else:
        return -2

    # Hour Shift
    if hour == 1 or hour == 2:
        shift.append(2)
    elif hour == 3:
        shift.append(5)
    elif hour == 4 or hour == 5:
        shift.append(8)
    elif hour == 6:
        shift.append(7)
    elif hour == 7 or hour == 8:
        shift.append(6)
    elif hour == 9:
        shift.append(3)
    elif hour == 10 or hour == 11:
        shift.append(0)
    elif hour == 12:
        shift.append(1)
    else:
        return -3

    return shift

# Main
plaintext = stdin.read()
time = "2:59:37"
shift = shift_calc(time)
plaintext = pad(plaintext)
ciphertext = ""
NUM_LAYERS = floor(log(len(plaintext), 9))
CURR_LAYER = 1
while CURR_LAYER <= NUM_LAYERS:
    ITERATIONS = 9**CURR_LAYER
    plaintext = swap(plaintext, shift, ITERATIONS)
    CURR_LAYER += 1
print(''.join(plaintext))