import numpy as np
import matplotlib.pyplot as plt
import pandas as pd, re
import math
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
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.5, random_state=10)


k = 2
a = []
y_knn = []
for i in range(len(X_test)):
    a = []
    for j in range(len(X_train)):
        distance = cosinus(X_test, X_train, i, j)
        a.append([distance, y_train[j]])
    
    a = sorted(a, key=lambda c: c[0])
    i = 0
    j = 0
    l = 0
    while(i < k ) and (j < k):
        if(a[l][1] == 0): i=i+1
        else:  j = j+1
        l = l + 1
    if(i == k): y_knn.append(0)
    else: y_knn.append(1)


y_knn = np.array(y_knn)
y_test = np.array(y_test)
accuracy = np.mean(y_knn == y_test)
print(y_test)
print(y_knn)
print(accuracy)



plt.figure(1, figsize=(4, 3))
plt.scatter(X[:, 0], X[:, 1], c = Y, edgecolors='k', cmap=plt.cm.Paired)
plt.xlabel('Рейтинг')
plt.ylabel('Цена')
plt.show()