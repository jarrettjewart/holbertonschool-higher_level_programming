#!/usr/bin/python3
for i range(0, 10):
    for j in range(1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        elif j > i:
            print("{}{}".format(i, j)' end=", ")
