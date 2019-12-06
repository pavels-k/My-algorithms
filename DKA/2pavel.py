print("Привет, это злая программа, которая определяет принадлежность строки w к языку, в котором после каждой подстроки 1^n, n > 0, w сразу содержит подстроку 0^i, i>n")
print("Введите строку w:")
w = input()
print('Ваша строка :',w)

w = w + '3'
counter = 1
q=[]
q.append('0')
q.append('1')
case = 1
s = []
s.append('$') 

print('Q=',q)
print('STACK=',s)

for number in w:
    if number.isalpha()==1:
        print("Обнаружена буква")
        break
    if (int(number) != 3) and (int(number) != 0) and (int(number) != 1):
        print('Символ не принадлежит алфавиту!')
        q.append('->REJECT')
        break
    elif case == 0:
       q.append('1')
       case = 1
       s.append('$') 

    elif case == 1:
        if (int(number) == 3) and (s[-1] == '$'):
            q.append('4')
            case = 4
            s.pop()
        elif int(number) == 1:
            q.append('2')
            case = 2
            s.append('a')
        elif int(number) == 0:
            q.append('1')

    elif case == 2:
        if (int(number) == 3) and (s[-1] == '$'):
            q.append('4')
            case = 4
            s.pop()
        elif int(number) == 1:
            q.append('2')
            case = 2
            s.append('a')
        elif (int(number) == 0) and (s[-1] == 'a'):
            q.append('2')
            case = 2
            s.pop()
        elif (int(number) == 0) and (s[-1] != 'a'):
            q.append('3')
            case = 3
    
    elif case == 3:
        if (int(number) == 3) and (s[-1] == '$'):
            q.append('4')
            case = 4
            s.pop()
        elif int(number) == 1:
            q.append('2')
            case = 2
            s.append('a')
        elif int(number) == 0:
            q.append('3')
    if case == 4:
        print('Q=',q)
        print('STACK=',s)
        break
    if(int(number)!= 3):
        print('Q=',q)
        print('STACK=',s)


if (q[-1] == '4'):
    print('ACCEPTED')
else:        
    print('REJECTED')