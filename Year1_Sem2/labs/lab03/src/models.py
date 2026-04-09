from base import Property


class RentalProperty(Property):

    def __init__(self, owner, price, rent_term, utilities, mortgage, tenant=None):
        super().__init__(owner, price, rent_term, utilities, mortgage, True)

        self._tenant = tenant
        self._remaining_months = rent_term if tenant else 0

    @property
    def tenant(self):
        return self._tenant

    @property
    def remaining_months(self):
        return self._remaining_months

    def rent_to(self, tenant):
        if not self.is_available():
            raise ValueError("Недвижимость недоступна для аренды")

        if self.has_debt:
            raise ValueError("Нельзя сдавать объект с долгами по ЖКХ")

        self._tenant = tenant
        self._rented = True
        self._remaining_months = self._rent_term

        print(f"Объект сдан в аренду. Арендатор: {tenant}")

    def next_month(self):
        if not self._rented:
            print("Объект не сдан")
            return

        self._remaining_months -= 1
        print(f"Прошел месяц. Осталось месяцев: {self._remaining_months}")

        if self._remaining_months <= 0:
            print("Срок аренды закончился")
            self.close_contract()

    def close_contract(self):
        super().close_contract()
        print("Договор аренды закрыт")
        self._tenant = None
        self._remaining_months = 0

    def is_available(self):
        return not self._rented and not self.has_debt

    def __str__(self):
        return f"[АРЕНДА] {super().__str__()} | арендатор={self._tenant} | осталось={self._remaining_months} мес."


class MortgageProperty(Property):

    def __init__(self, owner, price, rent_term, utilities, mortgage, interest_rate, years):
        super().__init__(owner, price, rent_term, utilities, mortgage, False)

        self._interest_rate = self._validate_rate(interest_rate)
        self._years_left = self._validate_years(years)

    def _validate_rate(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Некорректная ставка")
        return value

    def _validate_years(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Некорректный срок (годы)")
        return value

    @property
    def interest_rate(self):
        return self._interest_rate

    @property
    def years_left(self):
        return self._years_left

    def monthly_payment(self):
        payment = self._mortgage * (self._interest_rate / 100)
        print(f"Ежемесячный платёж: {payment}")
        return payment

    def pay_mortgage(self, amount):
        super().pay_mortgage(amount)

        print(f"Платёж внесён: {amount}")
        print(f"Остаток ипотеки: {self._mortgage}")

    def next_year(self):
        if self._years_left <= 0:
            print("Ипотека уже закрыта")
            return

        self._years_left -= 1
        print(f"Прошел год. Осталось лет: {self._years_left}")

        if self._years_left == 0:
            print("Срок ипотеки закончился")

    def is_available(self):
        return False
    
    def is_paid_off(self):
        return self._mortgage == 0

    def __str__(self):
        return f"[ИПОТЕКА] {super().__str__()} | ставка={self._interest_rate}% | осталось={self._years_left} лет"