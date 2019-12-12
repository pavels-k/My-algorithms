import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd, re
from sklearn.model_selection import train_test_split

df = pd.read_csv("data.csv")
df['Value'] = df['Value'].apply(
        lambda x: 'M' in x and float((re.findall('\d+\.*\d*', x)[0])) * pow(10, 6) or float(
            (re.findall('\d+\.*\d*', x)[0]).replace('.', '')) * pow(10, 3))

x_labels = ['Overall', 'Value', 'Club']
X = df.loc[:, x_labels]
X = X[(X.Club == 'FC Barcelona') | (X.Club == 'West Bromwich Albion')]
#X = X[X.Overall < 80]

X['Club'].replace('FC Barcelona','1',inplace=True)
X['Club'].replace('West Bromwich Albion','0',inplace=True)
Y = X['Club'].values
x_labels = ['Overall', 'Value']
X = X.loc[:, x_labels]
X = X.values
X = np.array(X)
Y = np.array(Y)
def evk(X_test, X_train, i, j):
    distance = math.sqrt((X_test[i][0] - X_train[j][0])**2 + (X_test[i][1] - X_train[j][1])**2)
    return distance

def modul_max(X_test, X_train, i, j):
    distance = max(abs(X_test[i][0] - X_train[j][0]), abs(X_test[i][1] - X_train[j][1]))
    return distance

def cosinus(X_test, X_train, i, j):
    distance = (X_test[i][0] * X_train[j][0] + X_test[i][1] * X_train[j][1])/((np.sqrt(X_test[i][0]**2 + X_test[i][1]**2)) * (np.sqrt(X_train[j][0]**2 + X_train[j][1]**2)))
    return distance



Y  = [int(item) for item in Y]

point = [65, 3000000]
#point = [80, 30000000]
k = 2
a = []
for i in range(len(X)):
    distance = math.sqrt((point[0] - X[i][0])**2 + (point[1] - X[i][1])**2)
    a.append([distance, Y[i]])
for i in range(len(X)):
    a = sorted(a, key=lambda c: c[0])
i = 0
j = 0
l = 0
while(i < k ) and (j < k):
    if(a[l][1] == 0): i=i+1
    else:  j = j+1
    l = l+1
if(i == k): print('blue')
else: print('orange')

plt.scatter(point[0], point[1], color='green', s=30, marker='o')        
plt.figure(1, figsize=(4, 3))
plt.scatter(X[:, 0], X[:, 1], c = Y, edgecolors='k', cmap=plt.cm.Paired)
plt.xlabel('Рейтинг')
plt.ylabel('Цена')
plt.show()
