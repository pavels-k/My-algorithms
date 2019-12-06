import numpy as np
import matplotlib.pyplot as plt
import pandas as pd, re
import math
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("data.csv")
df['Value'] = df['Value'].apply(
        lambda x: 'M' in x and float((re.findall('\d+\.*\d*', x)[0])) * pow(10, 6) or float(
            (re.findall('\d+\.*\d*', x)[0]).replace('.', '')) * pow(10, 3))

x_labels = ['Overall', 'Value', 'Real Face']
X = df.loc[:, x_labels]
X['Real Face'].replace('Yes','1',inplace=True)
X['Real Face'].replace('No','0',inplace=True)
Y = X['Real Face'].values
X = X.drop('Real Face', 1)

X = np.array(X)
notnan = []
cnt = 0
i = 0
while i < len(Y):
    if not pd.isnull(Y[i]):
        notnan[cnt:cnt] = [i]
        cnt = cnt + 1
    i = i+1

cnt = 0
newX = []
newY = []
for j in notnan:
    newX[cnt:cnt] = [X[j]]
    newY[cnt:cnt] = [Y[j]]
    cnt = cnt + 1

X = np.array(newX)
Y = newY

logreg = LogisticRegression()
logreg.fit(X, Y)

print(logreg.coef_)
print(logreg.intercept_)

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.figure(1, figsize=(4, 3))
plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)
plt.xlabel('Рейтинг')
plt.ylabel('Цена')
plt.xticks(())
plt.yticks(())
print(logreg.coef_[0][0])
plt.show()