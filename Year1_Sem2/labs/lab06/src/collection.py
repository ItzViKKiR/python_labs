class PropertyCollection:
    def __init__(self, items=None):
        if items is None:
            items = []
        self._items = list(items)

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return "\n".join(str(item) for item in self._items)

    def add(self, item):
        self._items.append(item)

    def sort_by(self, key_func):
        new_items = sorted(self._items, key=key_func)
        return PropertyCollection(new_items)

    def filter_by(self, predicate):
        new_items = [item for item in self._items if predicate(item)]
        return PropertyCollection(new_items)

    def apply(self, func):
        for item in self._items:
            func(item)
        return self