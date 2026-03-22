from model import Property


class District:

    def __init__(self):
        self._items = []

    def add(self, item):
        if not isinstance(item, Property):
            raise TypeError("only Property allowed")

        for obj in self._items:
            if obj.owner == item.owner and obj.price == item.price:
                raise ValueError("duplicate property")

        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def remove_at(self, index):
        if not isinstance(index, int):
            raise TypeError("index must be int")

        if index < 0 or index >= len(self._items):
            raise IndexError("index out of range")

        self._items.pop(index)

    def get_all(self):
        return self._items

    def find_by_owner(self, owner):
        return [x for x in self._items if x.owner == owner]

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self, key):
        self._items.sort(key=key)

    def sort_by_price(self):
        self._items.sort(key=lambda x: x.price)

    def get_available(self):
        new = District()
        for item in self._items:
            if item.is_available():
                new.add(item)
        return new

    def get_with_debt(self):
        new = District()
        for item in self._items:
            if item.has_debt:
                new.add(item)
        return new