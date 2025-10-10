def format_record(rec: tuple[str, str, float]) -> str:
    if type(rec) is not tuple:
        return TypeError('Введите кортеж')
    if len(rec)!=3:
        return ValueError('Ой-ой, каких-то данных не хватает!')
    if type(rec[2]) is not float:
        raise TypeError('Введите правильный балл GPA')
    if type(rec[1]) is not str:
        raise TypeError('Перепроверь свою группу')
    if type(rec[0]) is not str:
        raise TypeError('Думаю, нет человека, у которого имя не строка')
    name_parts=rec[0].strip().split()
    if len(name_parts)==3:
        surname, name, middle_name = name_parts
        return f"{surname.capitalize()} {name[0].upper()}.{middle_name[0].upper()}., гр. {rec[1].upper()}, GPA {rec[2]:.2f}"
    elif len(name_parts)==2:
        surname, name = name_parts
        return f"{surname.capitalize()} {name[0].upper()}., гр. {rec[1].upper()}, GPA {rec[2]:.2f}"
    else:
        raise ValueError('Введите правильное ФИ(О)')