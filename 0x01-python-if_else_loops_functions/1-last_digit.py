#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
l = abs(n) % 10
if n < 0:
    l = -l
if l > 5:
    print("last digit of {} is {} and is greater than 5".format(n, l))
elif l == 0:
    print("last digit of {} is {} and is 0".format(n, l))
else:
    print("last digit of {} is {} and is less than 6 and not 0".format(n, l))
