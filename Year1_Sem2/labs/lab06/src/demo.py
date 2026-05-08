from models import RentalProperty, MortgageProperty
from container import TypedCollection, Displayable, Scorable, D, S


def print_all(collection):
    print("\n".join(str(item) for item in collection.get_all()))


def demo_basics():
    print("=== Демонстрация типизированной коллекции ===")
    col: TypedCollection = TypedCollection()
    col.add(RentalProperty("Шубкин Александр Андреевич", 1000.0, 3, 0.0, 0.0))
    col.add(MortgageProperty("Немирович Марк Анатольевич", 200000.0, 12, 50.0, 80000.0, 4.0, 5))
    col.add(RentalProperty("Козлов Артём Александрович", 900.0, 2, 0.0, 0.0))
    col.add(MortgageProperty("Евсеев Данила Максимович", 180000.0, 6, 0.0, 0.0, 3.0, 7))
    col.add(RentalProperty("Идеи закончились", 1500.0, 1, 100.0, 0.0))
    print("Содержимое коллекции:")
    print_all(col)
    print()


def demo_find_filter_map():
    print("=== Демонстрация find, filter, map ===")
    col: TypedCollection = TypedCollection()
    col.add(RentalProperty("Шубкин Александр Андреевич", 1000.0, 3, 0.0, 0.0))
    col.add(MortgageProperty("Немирович Марк Анатольевич", 200000.0, 12, 50.0, 80000.0, 4.0, 5))
    col.add(RentalProperty("Козлов Артём Александрович", 900.0, 2, 0.0, 0.0))
    col.add(MortgageProperty("Евсеев Данила Максимович", 180000.0, 6, 0.0, 0.0, 3.0, 7))
    col.add(RentalProperty("Идеи закончились", 1500.0, 1, 100.0, 0.0))

    found = col.find(lambda x: x.owner.startswith("К"))
    print(f"Найден объект: {found}")
    not_found = col.find(lambda x: x.price < 500)
    print(f"Не найден (price < 500): {not_found}")

    filtered = col.filter(lambda x: x.is_available())
    print("Объекты доступные (is_available):")
    print_all(TypedCollection())  # затычка, выведу вручную
    for item in filtered:
        print(item)

    names = col.map(lambda x: x.owner)
    prices = col.map(lambda x: x.price)
    print("\nВладельцы (list[str]):", names)
    print("Цены (list[float]):", prices)
    print()


def demo_protocol_displayable():
    print("=== Демонстрация Protocol Displayable ===")
    collection: TypedCollection[D] = TypedCollection()
    collection.add(RentalProperty("Шубкин Александр Андреевич", 1000.0, 3, 0.0, 0.0))
    collection.add(MortgageProperty("Немирович Марк Анатольевич", 200000.0, 12, 50.0, 80000.0, 4.0, 5))
    collection.add(RentalProperty("Козлов Артём Александрович", 900.0, 2, 0.0, 0.0))
    print("Вызов display() у каждого элемента:")
    for item in collection.get_all():
        print(item.display())
    print()


def demo_protocol_scorable():
    print("=== Демонстрация Protocol Scorable ===")
    collection: TypedCollection[S] = TypedCollection()
    collection.add(RentalProperty("Шубкин Александр Андреевич", 1000.0, 3, 0.0, 0.0))
    collection.add(MortgageProperty("Немирович Марк Анатольевич", 200000.0, 12, 50.0, 80000.0, 4.0, 5))
    collection.add(RentalProperty("Козлов Артём Александрович", 900.0, 2, 0.0, 0.0))
    print("Вызов score() у каждого элемента:")
    for item in collection.get_all():
        print(f"{item.display()} -> score = {item.score()}")
    print()


if __name__ == "__main__":
    demo_basics()
    demo_find_filter_map()
    demo_protocol_displayable()
    demo_protocol_scorable()