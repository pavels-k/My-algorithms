import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import pandas as pd, re
import math

df = pd.read_csv("data/Students.csv")
x_labels = ["math score","reading score"]
X = df.loc[:, x_labels]
X = X.values
df.loc[df["lunch"] == "standard"] = 1
df.loc[df["lunch"] == "free/reduced"] = 0
y = df["lunch"].values
X = np.array(X)
y = np.array(y)

logreg = LogisticRegression()
logreg.fit(X, y)

x_values = [np.min(X[:, 0] - 5), np.max(X[:, 1] + 5)]
y_values = - (logreg.intercept_[0] + np.dot(logreg.coef_[0][0], x_values)) / logreg.coef_[0][1]

plt.plot(x_values, y_values, label='Decision Boundary')
plt.figure(1, figsize=(4, 3))
k = 0
m = 0
n = 0
for i in X:
    if y[k] == 0: 
        if m == 0:
            plt.scatter(i[0], i[1], c='cyan', edgecolors='k', cmap=plt.cm.Paired, label = 'Not entered')
            m = 1
        else:
            plt.scatter(i[0], i[1], c='cyan', edgecolors='k', cmap=plt.cm.Paired)

    else: 
        if n == 0:
            plt.scatter(i[0], i[1], c='red', edgecolors='k', cmap=plt.cm.Paired, label = 'Entered')
            n = 1
        else: plt.scatter(i[0], i[1], c='red', edgecolors='k', cmap=plt.cm.Paired)
    k = k + 1

plt.legend()
plt.xlabel('math score')
plt.ylabel('reading score')
plt.xticks(())
plt.yticks(())

plt.show()

k = 0
for i in X:
    phi = 1/(1+math.exp(-(logreg.intercept_[0]+logreg.coef_[0][0]*i[0]+logreg.coef_[0][1]*i[1])))
    print('Passing exam №', k,'math:', i[0],'reading:', i[1])
    k = k + 1

print('Enter the number of the dealer, for whom you want to know the probability of his receipt')
i = int(input())
while (i >=0) and (i <=1000):
    phi = 1/(1+math.exp(-(logreg.intercept_[0]+logreg.coef_[0][0]*X[i][0]+logreg.coef_[0][1]*X[i][1])))
    print(phi)
    i = int(input())
