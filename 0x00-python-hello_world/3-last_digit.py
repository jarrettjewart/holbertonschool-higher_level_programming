#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = ((number * -1) % 10) * -1
else:
    last_digit = number % 10

print("Last digit of {} is".format(number), end=" ")
if last_digit > 5:
    print("{} and if greater than 5".formt(last_digit))
elif last_digit == 0:
    print("{} and i 0".format(last_digit))
else:
    print("{} and is less than 6 and not 0".format(last_digit))
