import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

h = np.array([1, -1, 2, 0, 1])
x = np.array([3, 1, -3, 2, 0])
I = np.ones(len(h))
H = np.vstack([I, h])
print(H)
teta = linalg.inv(H @ H.transpose()) @ H @ x.transpose()
print('teta_MNK = ', teta)
tt = np.arange(min(h)-1,max(h)+1,0.1)
z = teta[0] + teta[1]*tt

x_ = []
for i in range(len(h)):
    x_.append(H[0,i] * teta[0] + H[1,i] * teta[1]) 
print(x_)
e_2 = 0
for i in range(len(x)):
    e_2 = e_2 + (x[i] - x_[i])**2 
print('E^ = ',e_2)

sigma_2 = e_2 * (1/(len(h)-2))
print('sigma = ',sigma_2)

print(np.mean(x))
sumX = 0
for i in x:
    sumX = sumX + (i - np.mean(x))**2 
print('summa X - X_',sumX)
R2 = 1  - (e_2 / sumX)
print("к. детерм. = ",R2)

'''
plt.scatter(h, x, color='red', s=40, marker='o')
plt.plot(tt, z)
plt.show()
'''