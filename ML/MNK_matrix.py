import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

h = np.array([-1, 0, 1, 2, 4])
x = np.array([2, 1, 0, -2, 3])
I = np.ones(len(h))
H = np.vstack([I, h])
print(H)
teta = linalg.inv(H @ H.transpose()) @ H @ x.transpose()
print(teta)
tt = np.arange(min(h)-1,max(h)+1,0.1)
z = teta[0] + teta[1]*tt

plt.scatter(h, x, color='red', s=40, marker='o')
plt.plot(tt, z)
plt.show()