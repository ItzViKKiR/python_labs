
def by_price(item):
    return item.price


def by_owner(item):
    return item.owner


def by_rent_term(item):
    return item.rent_term


def by_price_and_owner(item):
    return (item.price, item.owner)


def is_available(item):
    return item.is_available()


def has_debt(item):
    return item.has_debt


def is_rental(item):
    from models import RentalProperty
    return isinstance(item, RentalProperty)


def make_price_filter(max_price):
    def predicate(item):
        return item.price <= max_price
    return predicate


def apply_discount(factor):
    def func(item):
        item.price *= (1 - factor)
        return item
    return func


class DiscountStrategy:
    def __call__(self, item):
        item.price *= 0.9
        return item


class RentTermIncreaseStrategy:
    def __call__(self, item):
        if hasattr(item, '_rent_term'):
            item._rent_term += 1
        return item