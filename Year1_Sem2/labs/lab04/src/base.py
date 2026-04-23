from validate import *
from interfaces import Printable


class Property(Printable):

    properties_count = 0

    def __init__(self, owner, price, rent_term, utilities, mortgage, for_rent=True):
        self._owner = validate_owner(owner)
        self._price = validate_price(price)
        self._rent_term = validate_term(rent_term)
        self._utilities = validate_money(utilities)
        self._mortgage = validate_money(mortgage)
        self._for_rent = validate_bool(for_rent)
        self._rented = False
        Property.properties_count += 1

    def to_string(self):
        return self.__str__()

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = validate_owner(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = validate_price(value)

    @property
    def rent_term(self):
        return self._rent_term

    @rent_term.setter
    def rent_term(self, value):
        self._rent_term = validate_term(value)

    @property
    def utilities(self):
        return self._utilities

    @utilities.setter
    def utilities(self, value):
        self._utilities = validate_money(value)

    @property
    def mortgage(self):
        return self._mortgage

    @mortgage.setter
    def mortgage(self, value):
        self._mortgage = validate_money(value)

    @property
    def mortgage_active(self):
        return self._mortgage > 0

    @property
    def has_debt(self):
        return self._utilities > 0

    @property
    def rented(self):
        return self._rented

    def pay_utilities(self, amount):
        amount = validate_money(amount)
        if amount > self._utilities:
            raise ValueError("payment exceeds debt")
        self._utilities -= amount

    def pay_mortgage(self, amount):
        amount = validate_money(amount)
        if amount > self._mortgage:
            raise ValueError("payment exceeds mortgage")
        self._mortgage -= amount

    def is_available(self):
        return not self._rented

    def __str__(self):
        status = "yes" if self._rented else "no"
        return f"Владелец: {self._owner} | Цена: {self._price} | Арендован: {status} | ЖКХ: {self._utilities} | Ипотека: {self._mortgage}"