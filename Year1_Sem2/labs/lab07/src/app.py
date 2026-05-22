from base import Property
from container import TypedCollection
from models import RentalProperty, MortgageProperty

from exceptions import (
    PropertyNotFoundError,
    DuplicatePropertyError
)


class PropertyApp:

    def __init__(self) -> None:
        """
        создает приложение
        """

        self.collection: TypedCollection[Property] = TypedCollection()

    def add_rental(
        self,
        owner: str,
        price: float,
        rent_term: int,
        utilities: float,
        mortgage: float
    ) -> None:
        """
        добавляет аренду
        """

        if self.find_by_owner(owner) is not None:
            raise DuplicatePropertyError("Объект уже существует")

        self.collection.add(
            RentalProperty(
                owner,
                price,
                rent_term,
                utilities,
                mortgage
            )
        )

    def add_mortgage(
        self,
        owner: str,
        price: float,
        rent_term: int,
        utilities: float,
        mortgage: float,
        rate: float,
        years: int
    ) -> None:
        """
        добавляет ипотеку
        """

        if self.find_by_owner(owner) is not None:
            raise DuplicatePropertyError("Объект уже существует")

        self.collection.add(
            MortgageProperty(
                owner,
                price,
                rent_term,
                utilities,
                mortgage,
                rate,
                years
            )
        )

    def get_all(self) -> list[Property]:
        """
        возвращает все объекты
        """

        return self.collection.get_all()

    def find_by_owner(
        self,
        owner: str
    ) -> Property | None:
        """
        ищет по владельцу
        """

        return self.collection.find(
            lambda x: x.owner == owner
        )

    def change_owner(
        self,
        old_owner: str,
        new_owner: str
    ) -> None:
        """
        меняет владельца
        """

        item = self.find_by_owner(old_owner)

        if item is None:
            raise PropertyNotFoundError("Не найдено")

        item.owner = new_owner

    def delete_by_owner(
        self,
        owner: str
    ) -> None:
        """
        удаляет объект
        """

        item = self.find_by_owner(owner)

        if item is None:
            raise PropertyNotFoundError("Не найдено")

        self.collection.remove(item)

    def available_properties(
        self
    ) -> list[Property]:
        """
        фильтр доступных объектов
        """

        return self.collection.filter(
            lambda x: x.is_available()
        )

    def sort_by_price(
        self
    ) -> list[Property]:
        """
        сортировка по цене
        """

        return sorted(
            self.collection.get_all(),
            key=lambda x: x.price
        )

    def sort_by_owner(
        self
    ) -> list[Property]:
        """
        сортировка по владельцу
        """

        return sorted(
            self.collection.get_all(),
            key=lambda x: x.owner
        )

    def sort_by_term(
        self
    ) -> list[Property]:
        """
        сортировка по сроку
        """

        return sorted(
            self.collection.get_all(),
            key=lambda x: x.rent_term
        )