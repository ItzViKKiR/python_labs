def validate_string(value: str, field_name: str):
    if not isinstance(value, str):
        raise TypeError(f"{field_name} должен быть строкой")
    if not value.strip():
        raise ValueError(f"{field_name} не может быть пустым")


def validate_positive_number(value, field_name: str):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{field_name} должно быть числом")
    if value <= 0:
        raise ValueError(f"{field_name} должно быть > 0")


def validate_non_negative_number(value, field_name: str):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{field_name} должно быть числом")
    if value < 0:
        raise ValueError(f"{field_name} не может быть отрицательным")