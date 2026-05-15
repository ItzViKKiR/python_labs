from base import Property


class RentalProperty(Property):
    def __init__(
        self,
        owner: str,
        price: float,
        rent_term: int,
        utilities: float,
        mortgage: float,
        tenant: str | None = None
    ) -> None:
        super().__init__(
            owner,
            price,
            rent_term,
            utilities,
            mortgage,
            True
        )

        self._tenant: str | None = tenant
        self._remaining_months: int = rent_term if tenant else 0

    def calculate_payment(self) -> float:
        return self._price * self._rent_term

    def rent_to(self, tenant: str) -> None:
        if not self.is_available():
            raise ValueError("Недоступно")

        if self.has_debt:
            raise ValueError("Есть долг")

        self._tenant = tenant
        self._rented = True
        self._remaining_months = self._rent_term

    def is_available(self) -> bool:
        return not self._rented and not self.has_debt

    def __str__(self) -> str:
        return (
            f"[АРЕНДА] {super().__str__()} | "
            f"арендатор={self._tenant}"
        )


class MortgageProperty(Property):
    def __init__(
        self,
        owner: str,
        price: float,
        rent_term: int,
        utilities: float,
        mortgage: float,
        rate: float,
        years: int
    ) -> None:
        super().__init__(
            owner,
            price,
            rent_term,
            utilities,
            mortgage,
            False
        )

        self._rate: float = rate
        self._years: int = years

    def calculate_payment(self) -> float:
        return self._mortgage * (self._rate / 100.0)

    def is_available(self) -> bool:
        return self._mortgage == 0.0

    def __str__(self) -> str:
        return (
            f"[ИПОТЕКА] {super().__str__()} | "
            f"ставка={self._rate}%"
        )