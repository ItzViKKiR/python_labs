def validate_owner(value: str) -> str:

    if not isinstance(value, str):
        raise TypeError("owner must be string")

    if not value.strip():
        raise ValueError("owner empty")

    return value.strip()


def validate_price(value: float) -> float:

    if not isinstance(value, (int, float)):
        raise TypeError("price must be number")

    if value <= 0:
        raise ValueError("price must be > 0")

    return float(value)


def validate_money(value: float) -> float:

    if not isinstance(value, (int, float)):
        raise TypeError("money must be number")

    if value < 0:
        raise ValueError("money must be >= 0")

    return float(value)


def validate_term(value: int) -> int:

    if not isinstance(value, int):
        raise TypeError("term must be int")

    if value <= 0:
        raise ValueError("term must be > 0")

    return value


def validate_bool(value: bool) -> bool:

    if not isinstance(value, bool):
        raise TypeError("must be bool")

    return value


def validate_email(value: str) -> str:

    if not isinstance(value, str):
        raise TypeError("email must be string")

    value = value.strip()

    allowed_domains = (
        "@gmail.com",
        "@yandex.ru",
        "@edu.misis.ru"
        "@misis.ru"
    )

    if not value.endswith(allowed_domains):
        raise ValueError(
            "доступны только gmail.com, "
            "yandex.ru, edu.misis.ru, misis.ru"
        )

    return value