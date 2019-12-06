import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import pandas as pd, re
import math


df = pd.read_csv("./data.csv")
df['Value'] = df['Value'].apply(
    lambda x: 'M' in x and float((re.findall('\d+\.*\d*', x)[0])) * pow(10, 6) or float(
        (re.findall('\d+\.*\d*', x)[0]).replace('.', '')) * pow(10, 3))
x_labels = ['Overall','Value']
X = df.loc[:, x_labels]
X = X.values
df.loc[df['Real Face'] == 'Yes'] = 1
df.loc[df['Real Face'] == 'No'] = 0
y = df['Real Face'].values
admitted = df.loc[y == 1]
not_admitted = df.loc[y == 0]



X = np.array(X)
y = np.array(y)



logreg = LogisticRegression()

plt.legend()
plt.figure(1, figsize=(4, 3))
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.Paired)
plt.xlabel('Оценки за 1-ый экзамен')
plt.ylabel('Оценки за 2-ой экзамен')
plt.xticks(())
plt.yticks(())

plt.show()

for i in X:
    phi = 1/(1+math.exp(-(logreg.intercept_[0]+logreg.coef_[0][0]*i[0]+logreg.coef_[0][1]*i[1])))
    print('Вероятность поступить:', round(phi,3),'1-ый экзамен:', round(i[0],1),'2-ой экзамен:', round(i[1],1))