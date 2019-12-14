import math
import numpy as np 

for i in range(100,1000):

    number_1 = i % 10
    number_2 = i // 10 % 10
    number_3 = i // 10 // 10 % 1000
    #print(number_1, number_2, number_3)
    if (i / (number_1 + number_2 + number_3) == 19):
        print(i)

print()