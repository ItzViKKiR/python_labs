from validate import (
    validate_string,
    validate_positive_number,
    validate_non_negative_number
)


class Apartment:
    """
    Класс, описывающий квартиру.
    """

    # Атрибут класса
    property_type = "Квартира"

    def __init__(self, address: str, area: float, price: float,
                 mortgage_balance: float = 0.0,
                 utilities_debt: float = 0.0):

        # Валидация через отдельный файл
        validate_string(address, "Адрес")
        validate_positive_number(area, "Площадь")
        validate_positive_number(price, "Цена")
        validate_non_negative_number(mortgage_balance, "Ипотека")
        validate_non_negative_number(utilities_debt, "Долг ЖКХ")

        self._address = address
        self._area = area
        self._price = price
        self._mortgage_balance = mortgage_balance
        self._utilities_debt = utilities_debt
        self._is_available = True  # логическое состояние

    # -------------------------
    # Свойства
    # -------------------------

    @property
    def address(self):
        return self._address

    @property
    def area(self):
        return self._area

    @property
    def price(self):
        return self._price

    @property
    def mortgage_balance(self):
        return self._mortgage_balance

    @property
    def utilities_debt(self):
        return self._utilities_debt

    @property
    def is_available(self):
        return self._is_available

    # setter с валидацией
    @price.setter
    def price(self, value):
        validate_positive_number(value, "Цена")
        self._price = value

    # -------------------------
    # Бизнес-методы
    # -------------------------

    def pay_mortgage(self, amount: float):
        validate_non_negative_number(amount, "Платёж")

        if amount > self._mortgage_balance:
            raise ValueError("Нельзя оплатить больше остатка по ипотеке")

        self._mortgage_balance -= amount

    def pay_utilities(self, amount: float):
        validate_non_negative_number(amount, "Платёж")

        if amount > self._utilities_debt:
            raise ValueError("Нельзя оплатить больше долга по ЖКХ")

        self._utilities_debt -= amount

    def sell(self):
        if not self._is_available:
            raise ValueError("Квартира уже продана")

        if self._mortgage_balance > 0:
            raise ValueError("Нельзя продать квартиру с непогашенной ипотекой")

        self._is_available = False

    # -------------------------
    # Магические методы
    # -------------------------

    def __str__(self):
        status = "Доступна" if self._is_available else "Продана"

        return (
            f"{self.property_type}\n"
            f"Адрес: {self._address}\n"
            f"Площадь: {self._area:.2f} м²\n"
            f"Цена: {self._price:,.2f} ₽\n"
            f"Ипотека: {self._mortgage_balance:,.2f} ₽\n"
            f"Долг ЖКХ: {self._utilities_debt:,.2f} ₽\n"
            f"Статус: {status}"
        )

    def __repr__(self):
        return (
            f"Apartment(address='{self._address}', "
            f"area={self._area}, price={self._price})"
        )

    def __eq__(self, other):
        if not isinstance(other, Apartment):
            return False

        return (
            self._address == other._address and
            self._area == other._area and
            self._price == other._price
        )