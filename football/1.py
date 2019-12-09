import pandas as pd
import numpy as np
import collections

data = pd.read_csv("RPL.csv", encoding = 'cp1251', delimiter=';')
data.head()
RPL_2018_2019 = pd.read_csv('Team Name 2018 2019.csv', encoding = 'cp1251')
teamList = RPL_2018_2019['Team Name'].tolist()
tL = pd.array(['Анжи', 'Ахмат', 'Зенит', 'Краснодар', 'Локомотив', 'Ростов', 'Рубин', 'Спартак', 'Урал', 'Уфа', 'ЦСКА'])
print(teamList)

deleteTeam = [x for x in pd.unique(data['Соперник']) if x not in tL]
for name in deleteTeam:
    data = data[data['Команда'] != name]
    data = data[data['Соперник'] != name]
data = data.reset_index(drop=True)