from models import RentalProperty, MortgageProperty
from interfaces import Printable, Payable


def print_all(items: list[Printable]):
    print("\n=== Вывод объектов ===")
    for item in items:
        print(item.to_string())


def calculate_all(items: list[Payable]):
    print("\n=== Расчёт платежей ===")
    for item in items:
        print(item.calculate_payment())


# 🔹 Сценарий 1
def scenario_polymorphism():
    print("\n=== СЦЕНАРИЙ 1: Полиморфизм ===")

    objects = [
        RentalProperty("Шубкин Александр Андреевич", 1000, 3, 0, 0),
        MortgageProperty("Немирович Марк Анатольевич", 200000, 12, 0, 100000, 5, 10),
    ]

    print_all(objects)
    calculate_all(objects)


# 🔹 Сценарий 2
def scenario_isinstance():
    print("\n=== СЦЕНАРИЙ 2: Проверка интерфейсов ===")

    obj = RentalProperty("Шубкин Александр Андреевич", 1000, 3, 0, 0)

    print("Printable:", isinstance(obj, Printable))
    print("Payable:", isinstance(obj, Payable))


# 🔹 Сценарий 3
def scenario_collection_filter():
    print("\n=== СЦЕНАРИЙ 3: Фильтрация через интерфейсы ===")

    objects = [
        RentalProperty("Шубкин Александр Андреевич", 1000, 2, 0, 0),
        MortgageProperty("Немирович Марк Анатольевич", 200000, 12, 0, 80000, 4, 5),
        RentalProperty("Идеи закончились", 1500, 1, 100, 0),
    ]

    printable = [obj for obj in objects if isinstance(obj, Printable)]
    payable = [obj for obj in objects if isinstance(obj, Payable)]

    print_all(printable)
    calculate_all(payable)


if __name__ == "__main__":
    scenario_polymorphism()
    scenario_isinstance()
    scenario_collection_filter()