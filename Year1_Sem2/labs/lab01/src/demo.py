from model import Apartment


def main():
    print("=== Создание объекта ===")
    apt1 = Apartment(
        address="г. Москва, ул. Ленина, 10",
        area=60,
        price=10_000_000,
        mortgage_balance=1_000_000,
        utilities_debt=20_000
    )

    print(apt1)

    print("\n=== Setter ===")
    apt1.price = 9_500_000
    print("Новая цена:", apt1.price)

    print("\n=== Бизнес-логика ===")
    apt1.pay_utilities(5000)
    print("Остаток долга ЖКХ:", apt1.utilities_debt)

    print("\n=== Попытка продать с ипотекой ===")
    try:
        apt1.sell()
    except ValueError as e:
        print("Ошибка:", e)

    print("\n=== Погашаем ипотеку и продаём ===")
    apt1.pay_mortgage(1_000_000)
    apt1.sell()
    print("Статус доступности:", apt1.is_available)

    print("\n=== Некорректное создание ===")
    try:
        bad = Apartment("", -10, -100)
    except Exception as e:
        print("Ошибка:", e)

    print("\n=== Атрибут класса ===")
    print("Через класс:", Apartment.property_type)
    print("Через объект:", apt1.property_type)


if __name__ == "__main__":
    main()