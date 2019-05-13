# Abraxis
#
# Colby Austin
import sys
import re

file_name = sys.argv[1]                                         # reads the file
fn = open(file_name)                                            # opens the file
encrypted_file = fn.readlines()                                 # stores the files contents into a variable
dictionary = open('dictionary.txt')                             #

#the alphabets
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "
#


def findkey():                                                      #loops through all the keys in the dictionary.txt
    word = dictionary.readline()
    while(word != ''):
        if int(len(word)) == int(len(''.join(set(word)))):          #this eliminates all words with repeat characters
            entire_alphabet = (str(word.rstrip()) + str(ALPHABET))  #removes the newline character from the word and appends the alphabet to the end
            decrypted_alphabet = ""
            for character in entire_alphabet:                               #this loops through every character in the entire alphabet and removes the repeat characters
                if int(decrypted_alphabet.find(character)) == int(-1):
                    decrypted_alphabet += str(character)
            decrypted_file = decrypt(decrypted_alphabet,encrypted_file)     #decrypts the file with the decrypted alphabet that was just created
            percent_accuracy = plaintextfreqcheck(decrypted_file)           #runs the decrypted text through the plain text frequency check, bc its much faster
            if (percent_accuracy <= 1.0) & (percent_accuracy >= 0.50):      #if the accuracy is within between 100% and 50% then pass it on to the plain text word check bc its more thorough
                confidence = plaintextwordcheck(decrypted_file)             #passes the decrypted text into the plaintext word check
                if (0.90 < confidence) & (confidence < 1.0):  # if more than 90 percent of the words are matches print to the terminal
                    print ("confidence = %s" % (confidence))
                    print ("key = %s\n%s" %(word, decrypted_file))
                    break
        word = dictionary.readline()

def plaintextfreqcheck(decrypted_string):                   #frequency method
    e_count = 0
    expected_frequency = 0.1202
    adjusted_string = re.sub(r"[^a-z]", "", decrypted_string.lower())           #adjusts the decrypted string by removing special characters and making everything lowercase
    for letter in adjusted_string:
        if letter == 'e':
            e_count += 1
    total_characters = float(len(adjusted_string))
    if e_count > 0:
        frequency = float(e_count) / float(total_characters)
        percent_accuracy = (1 - float(abs(expected_frequency - frequency)) / float(expected_frequency))
    else:
        percent_accuracy = 2
    return percent_accuracy


def plaintextwordcheck(decrypted_string):                     #dictionary method
    word_count, word_match = 1.0, 0.0
    decrypted_list = decrypted_string.split()
    for decrypted_word in decrypted_list[:]:                                  # loops through every word in the decrypted string
        decrypted_word = re.sub(r"[^a-z']", "", decrypted_word.lower())
        with open('dictionary.txt') as dictionary:
            if decrypted_word in dictionary.read():
                word_match = float(word_match) + float(1)   # increase the word match count by 1
    end_of_word = False
    for i in range(len(decrypted_string)):
        if (decrypted_string[i] == ' ' or decrypted_string[i] == '\n' or decrypted_string[i] == '\t'):
            end_of_word = True
        elif end_of_word == True:
            end_of_word = False
            word_count = float(word_count) + float(1)  # increase the total world count by 1
    word_percentage = word_match / word_count  # calculates the percentage of matching words
    return word_percentage



def decrypt(decryption_alphabet, encrypted_text):
    decrypted_string = ''
    for encrypted_line in encrypted_text[:]:       #loops through each element in the list
        for character in encrypted_line:            #loops through each character in that element
            if character.isalpha():
                character_num = decryption_alphabet.find(character)
                decrypted_string += ALPHABET[character_num]
            else:
                decrypted_string += character
    return decrypted_string


findkey()
