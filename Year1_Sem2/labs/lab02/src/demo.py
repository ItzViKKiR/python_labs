from model import Property
from collection import District


def scenario_basic():

    d = District()

    p1 = Property("Шубкин Александр Андреевич", 100000, 12, 0, 20000)
    p2 = Property("Немирович Марк Анатольевич", 200000, 6, 5000, 10000)
    p3 = Property("Я не знаю какие еще есть преподы по проге", 150000, 12, 0, 0)

    d.add(p1)
    d.add(p2)
    d.add(p3)

    print("Все объекты:")
    for item in d:
        print(item)

    d.remove(p2)

    print("\nПосле удаления:")
    for item in d:
        print(item)


def scenario_search_and_len():

    d = District()

    p1 = Property("Шубкин Александр Андреевич", 100000, 12, 0, 20000)
    p2 = Property("Немирович Марк Анатольевич", 200000, 6, 5000, 10000)

    d.add(p1)
    d.add(p2)

    print("Количество объектов:", len(d))

    result = d.find_by_owner("Шубкин Александр Андреевич")

    print("Поиск:")
    for r in result:
        print(r)

    print("\nИтерация:")
    for item in d:
        print(item)


def scenario_sort_filter_index():

    d = District()

    p1 = Property("Шубкин Александр Андреевич", 300000, 12, 0, 20000)
    p2 = Property("Немирович Марк Анатольевич", 100000, 6, 5000, 10000)
    p3 = Property("Иванов Иван", 200000, 12, 0, 0)

    d.add(p1)
    d.add(p2)
    d.add(p3)

    print("Индексация:", d[0])

    d.sort_by_price()

    print("\nПосле сортировки:")
    for item in d:
        print(item)

    available = d.get_available()

    print("\nДоступные:")
    for item in available:
        print(item)

    debt = d.get_with_debt()

    print("\nС долгами:")
    for item in debt:
        print(item)

    d.remove_at(0)

    print("\nПосле удаления по индексу:")
    for item in d:
        print(item)


if __name__ == "__main__":

    scenario_basic()
    print("\n-----------------\n")

    scenario_search_and_len()
    print("\n-----------------\n")

    scenario_sort_filter_index()