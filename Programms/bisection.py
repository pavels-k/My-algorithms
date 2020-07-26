import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plt3d
from math import sqrt, cos, sin, radians
from sympy import symbols, poly, solve

x1 = [1, 4, 9]
B1 = 20
E1 = 60

x2 = [1, 8, 2]
B2 = 50
E2 = 60


E1 = radians(E1)
B1 = radians(B1)

r1 = sqrt(x1[0]**2 + x1[1]**2 + x1[2]**2)

x12 = r1 * cos(B1) * cos(E1)
y12 = r1 * sin(B1) * cos(E1)
z12 = r1 * sin(E1)

x12 = [x12, y12, z12]

x0 = []
y = []

for i in range(len(x1)):
    y.append(x1[i])
    y.append(x12[i])
    x0.append(y)
    y = []

E2 = radians(E1)
B2 = radians(B1)

r2 = sqrt(x2[0]**2 + x2[1]**2 + x2[2]**2)

x22 = r2 * cos(B2) * cos(E2)
y22 = r2 * sin(B2) * cos(E2)
z22 = r2 * sin(E2)

x22 = [x22, y22, z22]

x00 = []
y = []

for i in range(len(x1)):
    y.append(x2[i])
    y.append(x22[i])
    x00.append(y)
    y = []

a = [x12[0]-x1[0], y12-x1[1], z12 - x1[2]]
b = [x22[0]-x2[0], y22-x2[1], z22 - x2[2]]

n = np.cross(a, b)

t = symbols('t')
s = symbols('s')

par_x1 = (x12[0] - x1[0])*t + x1[0] 
par_y1 = (y12 - x1[1])*t + x1[1]
par_z1 = (z12 - x1[2])*t + x1[2]

par_x2 = (x22[0] - x2[0])*s + x2[0] 
par_y2 = (y22 - x2[1])*s + x2[1]
par_z2 = (z22 - x2[2])*s + x2[2]

H1H2 = [par_x2 - par_x1, par_y2 - par_y1, par_z2 - par_z1]

l = symbols('l')

system = []
system.append(H1H2[0] - n[0]*l)
system.append(H1H2[1] - n[1]*l)
system.append(H1H2[2] - n[2]*l)

sol = solve(system)

t = sol.get(t)
s = sol.get(s)
l = sol.get(l)

H1_x = (x12[0] - x1[0])*t + x1[0] 
H1_y = (y12 - x1[1])*t + x1[1]
H1_z = (z12 - x1[2])*t + x1[2]

H2_x = (x22[0] - x2[0])*s + x2[0] 
H2_y = (y22 - x2[1])*s + x2[1]
H2_z = (z22 - x2[2])*s + x2[2]

H = [[H1_x, H2_x], [H1_y, H2_y], [H1_z, H2_z]]
B_differences = [(H2_x - H1_x)/2, (H2_y - H1_y)/2, (H2_z - H1_z)/2]

B = [H[0][0] + B_differences[0], H[1][0] + B_differences[1], H[2][0] + B_differences[2]]
print(B)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(B[0],B[1],B[2], 'yellow')
ax.scatter(B[0],B[1],B[2], 'yellow')
ax.plot(x0[0], x0[1], x0[2], 'b')
ax.plot(x00[0], x00[1], x00[2], 'b')
ax.plot(H[0], H[1], H[2], 'r')


Hp = [[x1[0], H1_x], [x1[1], H1_y], [x1[2], H1_z]]
ax.plot(Hp[0], Hp[1], Hp[2], 'b')

Hp = [[x2[0], H2_x], [x2[1], H2_y], [x2[2], H2_z]]
ax.plot(Hp[0], Hp[1], Hp[2], 'b')

plt.show()