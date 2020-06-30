from numpy import *

b = array([[0, 1, 2, 3],
           [10, 11, 12, 13],
           [20, 21, 22, 23],
           [30, 31, 32, 33],
           [40, 41, 42, 43]])

for row in b:
    print(row)
    for el in row:
        print(" ", el)
