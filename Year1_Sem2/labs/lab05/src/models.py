from base import Property
from interfaces import Payable


class RentalProperty(Property, Payable):

    def __init__(self, owner, price, rent_term, utilities, mortgage, tenant=None):
        super().__init__(owner, price, rent_term, utilities, mortgage, True)
        self._tenant = tenant
        self._remaining_months = rent_term if tenant else 0

    def calculate_payment(self):
        return self._price * self._rent_term

    def rent_to(self, tenant):
        if not self.is_available():
            raise ValueError("Недоступно")

        if self.has_debt:
            raise ValueError("Есть долг")

        self._tenant = tenant
        self._rented = True
        self._remaining_months = self._rent_term

    def is_available(self):
        return not self._rented and not self.has_debt

    def __str__(self):
        return f"[АРЕНДА] {super().__str__()} | арендатор={self._tenant}"


class MortgageProperty(Property, Payable):

    def __init__(self, owner, price, rent_term, utilities, mortgage, rate, years):
        super().__init__(owner, price, rent_term, utilities, mortgage, False)
        self._rate = rate
        self._years = years

    def calculate_payment(self):
        return self._mortgage * (self._rate / 100)

    def is_available(self):
        return self._mortgage == 0

    def __str__(self):
        return f"[ИПОТЕКА] {super().__str__()} | ставка={self._rate}%"