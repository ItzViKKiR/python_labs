from model import Property


def scenario_rent_flow():

    p = Property("Шубкин Александр Андреевич", 1200, 12, 150, 20000, True)

    print("Создан объект недвижимости:")
    print(p)
    print("repr объекта:", repr(p))
    print("Доступна ли аренда:", p.is_available())

    print("\nЗаключаем договор аренды...")
    p.rental_contract()

    print("Статус после аренды:", p)
    print("Общая стоимость аренды:", p.total_rent_price())

    print("\nЗакрываем договор...")
    p.close_contract()

    print("Статус после закрытия договора:", p)
    print("Доступна ли аренда:", p.is_available())


def scenario_state_and_setters():

    p = Property("Немирович Марк Анатольевич", 300000, 12, 200, 50000, False)

    print("Информация о продаже:")
    print("Цена продажи:", p.sell_price())
    print("Есть ли ипотека:", p.mortgage_active)
    print("Есть ли долг по ЖКХ:", p.has_debt)

    print("\nИзменяем параметры через setter")

    p.price = 320000
    p.rent_term = 24

    print("Новая цена:", p.price)
    print("Новый срок аренды:", p.rent_term)

    print("\nПогашаем часть долгов")

    p.pay_utilities(100)
    p.pay_mortgage(10000)

    print("Остаток долга ЖКХ:", p.utilities)
    print("Остаток ипотеки:", p.mortgage)


def scenario_validation_and_comparison():

    print("Проверка валидации:")

    try:
        Property("", 1000, 12, 100, 20000)
    except Exception as e:
        print("Ошибка создания объекта:", e)

    p1 = Property("Шубкин Александр Андреевич", 1000, 12, 100, 20000)
    p2 = Property("Шубкин Александр Андреевич", 1000, 12, 100, 20000)

    print("\nСравнение объектов:")
    print("Объекты равны:", p1 == p2)

    print("\nДополнительная информация:")
    print("ЖКХ:", p1.check_utilities())
    print("Ипотека:", p1.check_mortgage())
    print("Владелец:", p1.owner_info())

    print("\nАтрибут класса:")
    print("Через класс:", Property.properties_count)
    print("Через объект:", p1.properties_count)


if __name__ == "__main__":

    scenario_rent_flow()
    print("\n---------------------\n")

    scenario_state_and_setters()
    print("\n---------------------\n")

    scenario_validation_and_comparison()