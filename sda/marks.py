import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import pandas as pd
import math




data = pd.read_csv("./marks.txt")
X = data.iloc[:, :-1] # Все кроме последнего
y = data.iloc[:, -1] # Последний

admitted = data.loc[y == 1] # для легенды
not_admitted = data.loc[y == 0]

X = np.array(X)
y = np.array(y)

logreg = LogisticRegression()
logreg.fit(X, y)


x_values = [np.min(X[:, 0] - 5), np.max(X[:, 1] + 5)]
y_values = - ( -0.2+logreg.intercept_[0] + np.dot(logreg.coef_[0][0], x_values)) / logreg.coef_[0][1] 
# формула

plt.scatter(admitted.iloc[:, 0], admitted.iloc[:, 1], s=10, label='Поступившие') # для легенды
plt.scatter(not_admitted.iloc[:, 0], not_admitted.iloc[:, 1], s=10, label='Не поступившие')

plt.plot(x_values, y_values, label='Граница принятия рещения')
plt.legend()
plt.figure(1, figsize=(4, 3))
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.Paired) # точки
plt.xlabel('Оценки за 1-ый экзамен')
plt.ylabel('Оценки за 2-ой экзамен')
plt.xticks(())
plt.yticks(())

plt.show()

for i in X:
    phi = 1/(1+math.exp(-(logreg.intercept_[0]+logreg.coef_[0][0]*i[0]+logreg.coef_[0][1]*i[1])))
    print('Вероятность поступить:', round(phi,3),'1-ый экзамен:', round(i[0],1),'2-ой экзамен:', round(i[1],1))