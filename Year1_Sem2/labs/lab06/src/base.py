from validate import (
    validate_owner,
    validate_price,
    validate_term,
    validate_money,
    validate_bool
)


class Property:
    properties_count: int = 0

    def __init__(
        self,
        owner: str,
        price: float,
        rent_term: int,
        utilities: float,
        mortgage: float,
        for_rent: bool = True
    ) -> None:
        self._owner: str = validate_owner(owner)
        self._price: float = validate_price(price)
        self._rent_term: int = validate_term(rent_term)
        self._utilities: float = validate_money(utilities)
        self._mortgage: float = validate_money(mortgage)
        self._for_rent: bool = validate_bool(for_rent)
        self._rented: bool = False

        Property.properties_count += 1

    @property
    def owner(self) -> str:
        return self._owner

    @owner.setter
    def owner(self, value: str) -> None:
        self._owner = validate_owner(value)

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        self._price = validate_price(value)

    @property
    def rent_term(self) -> int:
        return self._rent_term

    @rent_term.setter
    def rent_term(self, value: int) -> None:
        self._rent_term = validate_term(value)

    @property
    def utilities(self) -> float:
        return self._utilities

    @utilities.setter
    def utilities(self, value: float) -> None:
        self._utilities = validate_money(value)

    @property
    def mortgage(self) -> float:
        return self._mortgage

    @mortgage.setter
    def mortgage(self, value: float) -> None:
        self._mortgage = validate_money(value)

    @property
    def mortgage_active(self) -> bool:
        return self._mortgage > 0

    @property
    def has_debt(self) -> bool:
        return self._utilities > 0

    @property
    def rented(self) -> bool:
        return self._rented

    def pay_utilities(self, amount: float) -> None:
        amount = validate_money(amount)

        if amount > self._utilities:
            raise ValueError("payment exceeds debt")

        self._utilities -= amount

    def pay_mortgage(self, amount: float) -> None:
        amount = validate_money(amount)

        if amount > self._mortgage:
            raise ValueError("payment exceeds mortgage")

        self._mortgage -= amount

    def is_available(self) -> bool:
        return not self._rented

    def display(self) -> str:
        return str(self)

    def score(self) -> float:
        return float(self.price)

    def __str__(self) -> str:
        status = "yes" if self._rented else "no"

        return (
            f"Владелец: {self._owner} | "
            f"Цена: {self._price} | "
            f"Арендован: {status} | "
            f"ЖКХ: {self._utilities} | "
            f"Ипотека: {self._mortgage}"
        )