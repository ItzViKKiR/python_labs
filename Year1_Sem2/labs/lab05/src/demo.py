from models import RentalProperty, MortgageProperty
from collections import PropertyCollection
from strategies import (
    by_price,
    by_owner,
    by_rent_term,
    is_available,
    has_debt,
    make_price_filter,
    apply_discount,
    DiscountStrategy,
    RentTermIncreaseStrategy,
)


def print_step(title, collection):
    print(f"\n--- {title} ---")
    print(collection)


def scenario_chain():
    """Сценарий 1: цепочка filter → sort → apply с выводом каждого шага."""
    print("=== СЦЕНАРИЙ 1: Цепочка операций ===")

    items = [
        RentalProperty("Шубкин Александр Андреевич", 1000, 3, 0, 0),
        MortgageProperty("Немирович Марк Анатольевич", 200000, 12, 50, 80000, 4, 5),
        RentalProperty("Идеи закончились", 1500, 1, 100, 0),
        MortgageProperty("Евсеев Данила Максимович", 180000, 6, 0, 0, 3, 7),
        RentalProperty("Козлов Артём Александрович", 900, 2, 0, 0),
    ]
    col = PropertyCollection(items)
    print_step("Исходная коллекция", col)

    col_filtered = col.filter_by(is_available)
    print_step("После фильтрации (is_available)", col_filtered)

    col_sorted = col_filtered.sort_by(by_price)
    print_step("После сортировки по цене", col_sorted)

    col_discounted = col_sorted.apply(apply_discount(0.1))
    print_step("После применения скидки 10%", col_discounted)


def scenario_strategy_replacement():
    """Сценарий 2: замена стратегии сортировки без изменения кода коллекции."""
    print("\n=== СЦЕНАРИЙ 2: Взаимозаменяемые стратегии ===")

    items = [
        RentalProperty("Шубкин Александр Андреевич", 1000, 3, 0, 0),
        MortgageProperty("Немирович Марк Анатольевич", 200000, 12, 50, 80000, 4, 5),
        RentalProperty("Идеи закончились", 1500, 1, 100, 0),
        MortgageProperty("Евсеев Данила Максимович", 180000, 6, 0, 0, 3, 7),
        RentalProperty("Козлов Артём Александрович", 900, 2, 0, 0),
    ]
    col = PropertyCollection(items)

    sorted_by_price = col.sort_by(by_price)
    print_step("Сортировка по цене", sorted_by_price)

    sorted_by_owner = col.sort_by(by_owner)
    print_step("Сортировка по владельцу", sorted_by_owner)

    sorted_by_term = col.sort_by(by_rent_term)
    print_step("Сортировка по сроку аренды", sorted_by_term)


def scenario_callable_strategy():
    """Сценарий 3: демонстрация callable-объекта как стратегии."""
    print("\n=== СЦЕНАРИЙ 3: Callable-стратегии ===")

    items = [
        RentalProperty("Шубкин Александр Андреевич", 1000, 3, 0, 0),
        MortgageProperty("Немирович Марк Анатольевич", 200000, 12, 50, 80000, 4, 5),
        RentalProperty("Козлов Артём Александрович", 900, 2, 0, 0),
    ]
    col = PropertyCollection(items)
    print_step("Исходная коллекция", col)

    discount_strategy = DiscountStrategy()
    col.apply(discount_strategy)
    print_step("После DiscountStrategy (10% скидка)", col)

    increase_term = RentTermIncreaseStrategy()
    col.apply(increase_term)
    print_step("После RentTermIncreaseStrategy (+1 к сроку аренды)", col)


if __name__ == "__main__":
    scenario_chain()
    scenario_strategy_replacement()
    scenario_callable_strategy()