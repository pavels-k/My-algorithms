print("Привет, это злая программа, которая определяет принадлежность строки w к языку, который содержит чётное число 0")
print("Введите строку w:")
w = input()
print('Ваша строка :',w)

q=[]
q.append('q0')
case = 0

for number in w:
    if number.isalpha()==1:
        print("Обнаружена буква")
        q.append('->REJECT')
        break
    if int(number) != 0 and int(number) != 1:
        print('Символ не принадлежит алфавиту!')
        q.append('->REJECT')
        break
    elif case == 0:
        if int(number) == 1:
            q.append('->q1')
            case = 1
        elif int(number) == 0:
            q.append('->q2')
            case = 2     
    elif case == 1:
        if int(number) == 1:
            q.append('->q1')
            case = 1
        elif int(number) == 0:
            q.append('->q2')
            case = 2
    elif case == 2:
        if int(number) == 1:
            q.append('->q2')
            case = 2
        elif int(number) == 0:
            q.append('->q1')
            case = 1

if (q[-1] == '->REJECT'):
    print(q)
elif (q[-1]!='->q2'):
    q.append('->ACCEPT')
    print(q)
else: 
    q.append('->REJECT')       
    print(q)