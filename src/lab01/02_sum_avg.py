a=input('Число а: ')
b=input("Число б: ")
a=float(a.replace(',','.'))
b=float(b.replace(',','.'))
sum=a+b
avg=(a+b)/2
print('Сумма =',round(sum,2),'; Среднее арифметическое =',round(avg,2))
