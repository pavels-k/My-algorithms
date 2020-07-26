import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

h = np.array([1, -1, 2, 0, 1])
x = np.array([3, 1, -3, 2, 0])
I = np.ones(len(h))
H = np.vstack([I, h])
teta = linalg.inv(H @ H.transpose()) @ H @ x.transpose()
print('teta_MNK = ', teta)
tt = np.arange(min(h)-1,max(h)+1,0.1)
z = teta[0] + teta[1]*tt

plt.scatter(h, x, color='red', s=40, marker='o')
plt.plot(tt, z)
plt.show()
