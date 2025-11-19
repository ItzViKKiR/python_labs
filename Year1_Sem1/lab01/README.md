# Лабораторная работа №1
### Задание 1
``` python
print("Сколько тебе будет через год?")
name=str(input('Имя: '))
age=int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age +1}.')
```
![Результат 1го кода](/Year1_Sem1/lab01/images/lab1_ex1.png)

### Задание 2
``` python
a=input('Число а: ')
b=input("Число б: ")
a=float(a.replace(',','.'))
b=float(b.replace(',','.'))
sum=a+b
avg=(a+b)/2
print('Сумма =',round(sum,2),'; Среднее арифметическое =',round(avg,2))
```
![Результат 2го кода](/Year1_Sem1/lab01/images/lab1_ex2.png)

### Задание 3
``` python
price=float(input('Введите цену:'))
discount=float(input('Введите скидку:'))
vat=float(input('Введите НДС:'))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {'%.2f' % base} ₽')
print(f'НДС: {'%.2f' % vat_amount} ₽')
print(f'Итого к оплате: {'%.2f' % total} ₽')
```
![Результат 3го кода](/Year1_Sem1/lab01/images/lab1_ex3.png)

### Задание 4
``` python
print("Добро пожаловать в переводчик минут.")
print("Данный код переводит минуты в формат ЧЧ:ММ.")
m=int(input('Введите кол-во минут: '))
hours=m//60
minutes=m%60
print(f'Результат перевода:{m//60}:{m%60:02d}')
```
![Результат 4 кода](/Year1_Sem1/lab01/images/lab1_ex4.png)

### Задание 5
``` python
print('Давайте узнаем ваши инициалы')
fullname=str(input('ФИО:'))
name=fullname.split(' ')
newname=[new for new in name if new]
initials=[newname[num][0].upper() for num in range(len(newname))]
print('Инициалы: ','.'.join(initials))
print('Длина (символов): ',len(' '.join(newname)))
```

![Результат 5 кода](/Year1_Sem1/lab01/images/lab1_ex5.png)

## Задания со звездочкой
### Задание 6
``` python
members = int(input('in_1: '))
ochno = 0
zaochno = 0
for i in range(members):
    member = input(f'in_{i+2}: ')
    if 'True' in member:
        ochno +=1
    else:
        zaochno+=1
print(f'out: {ochno} {zaochno}')
```

![Результат 6 кода](/Year1_Sem1/lab01/images/lab1_ex6.png)

### Задание 7
``` python
vxod = input('in: ')
word = ''
index1 = 0 
index2 = 0

for i in range(len(vxod)):
    if vxod[i].isupper():
        index1 = i 
        break
    else:
        continue 
for i in range(len(vxod)):
    if vxod[i] in '0123456789':
        index2 = i+1
        break
    else:
        continue
shag = index2 - index1
for i in range(index1,len(vxod),shag):
    word+=vxod[i]
print(f'out: {word}')
```
![Результат 7 кода](/Year1_Sem1/lab01/images/lab1_ex7.png)