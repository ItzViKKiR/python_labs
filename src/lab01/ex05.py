print('Давайте узнаем ваши инициалы')
fullname=str(input('ФИО:'))
name=fullname.split(' ')
newname=[new for new in name if new]
initials=[newname[num][0] for num in range(len(newname))]
print('Инициалы: ','.'.join(initials))
print('Длина (символов): ',len(' '.join(newname)))