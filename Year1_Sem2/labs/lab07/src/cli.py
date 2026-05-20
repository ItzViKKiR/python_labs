# cli.py

from app import PropertyApp
from storage import save, load
from validate import validate_email

from exceptions import (
    PropertyNotFoundError,
    DuplicatePropertyError
)



DATA_FILE = "properties.json"


def print_menu() -> None:

    print("\n========= СИСТЕМА НЕДВИЖИМОСТИ =========")

    print("1. Зарегистрировать недвижимость")
    print("2. Показать всю недвижимость")
    print("3. Найти по владельцу")
    print("4. Поменять владельца")
    print("5. Заказать выписку ЕГРН")
    print("6. Удалить объект")
    print("7. Фильтр доступной недвижимости")
    print("8. Сортировка недвижимости")

    print("0. Выход")

    print("========================================")


def print_properties(items) -> None:

    if not items:
        print("Пусто")
        return

    for item in items:
        print(item)


def cancel_to_menu() -> bool:

    answer = input(
        "\nВернуться в главное меню? (y/n): "
    )

    return answer.lower() == "y"


def input_string(message: str):

    value = input(
        f"{message} "
        "(0 - отмена): "
    )

    if value == "0":

        if cancel_to_menu():
            return None

        return input_string(message)

    return value


def input_int(
    message: str,
    allowed: tuple | None = None
):

    while True:

        value = input(
            f"{message} "
            "(0 - отмена): "
        )

        if value == "0":

            if cancel_to_menu():
                return None

            continue

        try:

            value = int(value)

            if allowed is not None:

                if value not in allowed:

                    print(
                        f"Ошибка: допустимо "
                        f"{allowed}"
                    )

                    continue

            return value

        except ValueError:

            print(
                "Ошибка: введите число"
            )


def input_float(message: str):

    while True:

        value = input(
            f"{message} "
            "(0 - отмена): "
        )

        if value == "0":

            if cancel_to_menu():
                return None

            continue

        try:

            return float(value)

        except ValueError:

            print(
                "Ошибка: введите число"
            )


def run_cli():

    app = PropertyApp()

    data = load(DATA_FILE)

    for item in data:
        app.collection.add(item)

    while True:

        print_menu()

        try:

            choice = int(
                input("Выберите пункт: ")
            )

            if choice not in (
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8
            ):

                print(
                    "Ошибка: неверный пункт меню"
                )

                continue

        except ValueError:

            print(
                "Ошибка: введите число"
            )

            continue

        try:

            if choice == 1:

                print("\n1. Аренда")
                print("2. Ипотека")

                property_type = input_int(
                    "Тип недвижимости",
                    (1, 2)
                )

                if property_type is None:
                    continue

                owner = input_string(
                    "Владелец"
                )

                if owner is None:
                    continue

                price = input_float(
                    "Цена"
                )

                if price is None:
                    continue

                rent_term = input_int(
                    "Срок"
                )

                if rent_term is None:
                    continue

                utilities = input_float(
                    "ЖКХ"
                )

                if utilities is None:
                    continue

                mortgage = input_float(
                    "Ипотека"
                )

                if mortgage is None:
                    continue

                if property_type == 1:

                    app.add_rental(
                        owner,
                        price,
                        rent_term,
                        utilities,
                        mortgage
                    )

                elif property_type == 2:

                    rate = input_float(
                        "Ставка"
                    )

                    if rate is None:
                        continue

                    years = input_int(
                        "Лет"
                    )

                    if years is None:
                        continue

                    app.add_mortgage(
                        owner,
                        price,
                        rent_term,
                        utilities,
                        mortgage,
                        rate,
                        years
                    )

                print(
                    "Недвижимость добавлена"
                )

            elif choice == 2:

                print_properties(
                    app.get_all()
                )

            elif choice == 3:

                owner = input_string(
                    "Введите владельца"
                )

                if owner is None:
                    continue

                item = app.find_by_owner(
                    owner
                )

                if item is None:

                    print("Не найдено")

                else:

                    print(item)

            elif choice == 4:

                old_owner = input_string(
                    "Старый владелец"
                )

                if old_owner is None:
                    continue

                new_owner = input_string(
                    "Новый владелец"
                )

                if new_owner is None:
                    continue

                confirm = input(
                    "Подтвердить? (y/n): "
                )

                if confirm.lower() == "y":

                    app.change_owner(
                        old_owner,
                        new_owner
                    )

                    print(
                        "Владелец изменен"
                    )

            elif choice == 5:

                owner = input_string(
                    "Введите владельца"
                )

                if owner is None:
                    continue

                item = app.find_by_owner(
                    owner
                )

                if item is None:

                    print("Не найдено")

                else:

                    while True:

                        email = input(
                            "Укажите email "
                            "(0 - отмена): "
                        )

                        if email == "0":

                            if cancel_to_menu():
                                break

                            continue

                        try:

                            email = validate_email(
                                email
                            )

                            print(
                                "\n===== ВЫПИСКА ЕГРН ====="
                            )

                            print(item)

                            print(
                                "========================"
                            )

                            print(
                                f"\nВыписка "
                                f"отправлена "
                                f"на почту "
                                f"{email}"
                            )

                            break

                        except ValueError as error:

                            print(
                                "Ошибка:",
                                error
                            )

            elif choice == 6:

                owner = input_string(
                    "Введите владельца"
                )

                if owner is None:
                    continue

                confirm = input(
                    "Удалить объект? "
                    "(y/n): "
                )

                if confirm.lower() == "y":

                    app.delete_by_owner(
                        owner
                    )

                    print(
                        "Объект удален"
                    )

            elif choice == 7:

                filtered = (
                    app.available_properties()
                )

                print_properties(
                    filtered
                )

            elif choice == 8:

                print("\n1. По владельцу")
                print("2. По цене")
                print("3. По сроку")

                sort_choice = input_int(
                    "Выбор",
                    (1, 2, 3)
                )

                if sort_choice is None:
                    continue

                if sort_choice == 1:

                    result = (
                        app.sort_by_owner()
                    )

                elif sort_choice == 2:

                    result = (
                        app.sort_by_price()
                    )

                else:

                    result = (
                        app.sort_by_term()
                    )

                print_properties(
                    result
                )

            elif choice == 0:

                confirm = input(
                    "Сохранить данные "
                    "и выйти? (y/n): "
                )

                if confirm.lower() == "y":

                    save(
                        app.collection,
                        DATA_FILE
                    )

                    print(
                        "Данные сохранены"
                    )

                    print("Выход...")

                    break

        except DuplicatePropertyError as error:

            print(error)

        except PropertyNotFoundError as error:

            print(error)

        except ValueError as error:

            print("Ошибка:", error)