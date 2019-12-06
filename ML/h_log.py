import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


h1 = [7, 1, 3, 1, 0, 3, 8, 4, 5, 8, 2, 3, 3, 4]
h2 = [1, 0, 2, 5, 3, 2, 2, 7, 9, 3, 0, 2, 4, 1]
X = np.column_stack((h1 , h2))
Y = [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1]


logreg = LogisticRegression()
logreg.fit(X, Y)


x_values = [np.min(X[:, 0] - 5), np.max(X[:, 1] + 5)]
y_values = - ( logreg.intercept_[0] + np.dot(logreg.coef_[0][0], x_values)) / logreg.coef_[0][1]

plt.plot(x_values, y_values, label='Граница принятия рещения')
plt.legend()
plt.figure(1, figsize=(4, 3))
plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)
plt.xlabel('X')
plt.ylabel('Y')
plt.xticks(())
plt.yticks(())

plt.show()