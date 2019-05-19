# Epidemic Matrix Cipher

This is the final project for The Epidemics in Applied Cryptography taken Spring 2019

## Overview

## Steps

### Step 1
* In Step 1, each team will be given the first 3 encrypted messages and the timestamps of when each was sent.
* Teams will be expected to decrypt the messages, either by hand or using programs that they come up with.
* These messages are fairly easy to read, but the way the messages are scrambled is a hint as two how the cipher works.
* By the end of this step, the teams should realize that the messages are rearranged in sets of 9 characters and have something to do with the timestamps.

### Step 2
* In this step, the teams will be given a longer message and a timestamp
* The larger message will contain more than 81 characters. This is large enough to create 9 of the 3x3 matrices. Enough to make a bigger one ;)
* The new component introduced in this step is the concept of each 3x3 matrix being nested inside of larger matrices that will then be shifted as well.
* Teams will also need to deal with (or ignore?) the hanging strings that don't fit into the largest layer of the matrix.
* At this point, we can give away some clues as to the shift as it is less important than seeing that there can be multiple layers.

### Step 3
* In the final step, teams will receive a gigantic message. It will definitely use 3 or more layers.
* Teams that make it this far should now know that substrings of 9 characters make up 3x3 matrices that are nested inside larger 3x3 matrices.
* They should also realize that each level of the giant matrix shifts in accordance to the time that the matrix was encrypted.
* Ultimately, we want to see that the teams that complete the challenge know what the final message contains.

