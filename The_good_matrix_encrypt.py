# Matrix Encryption
# by: The Epidemics

# For the 3x3 array


def swap(plaintext, shift):
    for i in shift:
            temp = plaintext[4]
            plaintext[4] = plaintext[i]
            plaintext[i] = temp
    return plaintext


def pad(plaintext):
    padding = "#"
    n = len(plaintext)%9
    if n != 0:
        num_pad = 9 - n
        while num_pad > 0:
            plaintext = plaintext + padding
            num_pad -= 1
    return plaintext


def loop_calc(text):
    n, i, string_length = len(text), 0, []
    while (9 ** i) <= n:
        string_length.append(9**i)
        i += 1
    return string_length


# Calculating the shift
def shift_calc(time):
    time = time.split(":")
    hour, minute, second, shift = int(time[0]), int(time[1]), int(time[2]), []
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
        return -1

    # Minute Shift
    if 5 <= minute <= 10:
        shift.append(2)
    elif 11 <= minute <= 19:
        shift.append(5)
    elif 20 <= minute <= 25:
        shift.append(8)
    elif 26 <= minute <= 34:
        shift.append(7)
    elif 35 <= minute <= 40:
        shift.append(6)
    elif 41 <= minute <= 49:
        shift.append(3)
    elif 50 <= minute <= 55:
        shift.append(0)
    elif (56 <= minute <= 59) or (0 <= minute <= 4):
        shift.append(1)
    else: return -2

    # Second Shift
    if 5 <= second <= 10:
        shift.append(2)
    elif 11 <= second <= 19:
        shift.append(5)
    elif 20 <= second <= 25:
        shift.append(8)
    elif 26 <= second <= 34:
        shift.append(7)
    elif 35 <= second <= 40:
        shift.append(6)
    elif 41 <= second <= 49:
        shift.append(3)
    elif 50 <= second <= 55:
        shift.append(0)
    elif (56 <= second <= 59) or (0 <= second <= 4):
        shift.append(1)
    else: return -3

    return shift


# Main
plaintext = "a23456789b23456789c23456789d23456789e23456789f23456789g23456789h23456789i23456789j23456789k23456789l23456789m23456789n23456789o23456789p23456789q23456789r23456789s23456789t23456789u23456789v23456789w23456789x23456789y23456789z23456789"
time = "12:37:00"
shift = shift_calc(time)
text = pad(plaintext)
string_length = loop_calc(text)

for n in string_length:
    broken_text = []
    for i in range(0, len(text), n):
        broken_text.append(text[i:i+n])
    swapped_text = []
    for i in range(0, len(broken_text), 9):
        if(len(broken_text[i:i+9])) == 9:
            swapped_text.append(swap(broken_text[i:i+9], shift))
        else:
            swapped_text.append(broken_text[i:])
    text = ""
    for i in swapped_text:
        text = text + "".join(i)
    print(text)
