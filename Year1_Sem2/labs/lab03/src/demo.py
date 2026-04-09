from models import RentalProperty, MortgageProperty


def scenario_rent_lifecycle():
    print("=== СЦЕНАРИЙ 1: Жизненный цикл аренды ===")

    flat = RentalProperty(
        "Шубкин Александр Андреевич",
        120000,
        6,      # срок аренды
        300,    # долг ЖКХ
        0
    )

    print("\nСоздан объект:")
    print(flat)

    print("\nПробуем сдать с долгом:")
    try:
        flat.rent_to("Иванов")
    except Exception as e:
        print("Ошибка:", e)

    print("\nГасим долг...")
    flat.pay_utilities(300)

    print("\nСдаём квартиру:")
    flat.rent_to("Есть ли еще преподы по проге?")

    print(flat)

    print("\nПроходит несколько месяцев:")
    for _ in range(3):
        flat.next_month()

    print("\nТекущее состояние:")
    print(flat)

    print("\Пытаемся дожить до конца договора:")
    while not flat.is_available():
        flat.next_month()

    print("\nИтог:")
    print(flat)


def scenario_mortgage_lifecycle():
    print("\n=== СЦЕНАРИЙ 2: Жизнь ипотеки ===")

    house = MortgageProperty(
        "Немирович Марк Анатольевич",
        500000,
        12,
        0,
        120000,   # долг
        5,        # %
        6         # лет
    )

    print("\nСоздан объект:")
    print(house)

    print("\nСчитаем платёж:")
    house.monthly_payment()

    print("\nПлатим несколько месяцев:")

    print("\nПроходит несколько лет:")

    for _ in range(2):
        house.next_year()
        house.pay_mortgage(20000)

    print("\nТекущее состояние:")
    print(house)

    print("\nДосрочно закрываем ипотеку:")
    house.pay_mortgage(house.mortgage)

    print("Ипотека закрыта:", house.is_paid_off())


def scenario_polymorphism_smart():
    print("\n=== СЦЕНАРИЙ 3: Полиморфизм ===")

    objects = [
        RentalProperty("Шубкин Александр Андреевич", 100000, 3, 0, 0),
        RentalProperty("Немирович Марк Анатольевич", 150000, 3, 200, 0),
        MortgageProperty("У меня закончились идеи", 300000, 12, 0, 80000, 4, 5),
    ]

    for obj in objects:
        print("\nОбъект:", obj)

        print("Доступен:", obj.is_available())

        # полиморфизм
        if hasattr(obj, "monthly_payment"):
            obj.monthly_payment()

        if hasattr(obj, "rent_to") and obj.is_available():
            obj.rent_to("Тестовый арендатор")
            print("После сдачи:", obj)


if __name__ == "__main__":
    scenario_rent_lifecycle()
    scenario_mortgage_lifecycle()
    scenario_polymorphism_smart()