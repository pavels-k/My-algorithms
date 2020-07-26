def len_int (x):
    if x == 0:
        return 1
    len_ = 0
    while x:
        x //= 10
        len_  += 1
    return (len_)

a = int(input())
b = 3 * int(input())
c = a*b
j = 0
lenc = len_int(c)
i = 0
massiv = []

for k in range(a):
    for l in range(b):
        massiv.append(i)
        i = i + 1
i = 0

for k in range(a):
    for l in range(b):
        if( (massiv[l+k*b]//b) % 2 == 0):
            tmp = massiv[l+k*b]
            while((len_int(c) - len_int(tmp) != 0)):
                print(' ', end=''),
                tmp = tmp * 10
                if tmp == 0: tmp = 10
            print(' ', end=''),
            print(massiv[l+k*b], end=''),
        else: 
            tmp = massiv[(k+1)*b - l-1]
            while((len_int(c) - len_int(tmp) != 0)):
                print(' ', end=''),
                tmp = tmp * 10
                if tmp == 0: tmp = 10
            print(' ', end=''),
            print(massiv[(k+1)*b - l-1], end=''),
        
        if l != 0:
            if (l+1)/b == 1: print('')