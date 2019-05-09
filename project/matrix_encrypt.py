def little_encrypt(plaintext, shift):   #the issue is somewhere in here
    plaintext = list(plaintext)
    num_loops = len(plaintext) / 9
    for i in shift:
        j = 1
        while j <= num_loops:               #I believe it is inside of this while loop
            temp = plaintext[(j * (num_loops - 1)) + 4]
            plaintext[(j * (num_loops - 1)) + 4] = plaintext[(j * (num_loops - 1)) + i]
            plaintext[(j * (num_loops - 1)) + i] = temp
            print(plaintext)
            j += 1
    return plaintext

def big_encrypt(pet, shift):
    pass

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
        return -1

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
        return -3

    return shift

#main:
plaintext = "Test this, douche"
time = "8:59:37"
shift = shift_calc(time)
print(shift)
plaintext = pad(plaintext)
print(plaintext)
pet = little_encrypt(plaintext, shift)
print ("".join(pet))
#encrypted_text = big_encrypt(pet,shift)
#print(encrypted_text)
