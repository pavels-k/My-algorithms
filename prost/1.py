import math
import numpy as np 

gen = (x for x in range(10000) if x not in [0,1,2,3])
prost = []
for i in gen:
    #print(i)
    k = 0
    for j in range(2,i-1):
        if i % j == 0: k = 1
    if (k == 0): 
        prost.append(i)
        #print(i)
j = 0
for i in prost:
    if i - j == 4: print(j, i)
    j = i
        