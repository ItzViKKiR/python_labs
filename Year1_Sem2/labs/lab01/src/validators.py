import re
from typing import Any
from datetime import datetime

def validate_string(value: Any, field_name: str, min_len=1, max_len=200) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field_name} должен быть строкой")
    stripped = value.strip()
    if not stripped:
        raise ValueError(f"{field_name} не может быть пустым")
    if len(stripped) < min_len:
        raise ValueError(f"{field_name} должен содержать минимум {min_len} символов")
    if len(stripped) > max_len:
        raise ValueError(f"{field_name} не может быть длиннее {max_len} символов")
    return stripped

def validate_positive_float(value: Any, field_name: str, allow_zero=False) -> float:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{field_name} должен быть числом")
    if value != value or value == float('inf') or value == float('-inf'):
        raise ValueError(f"{field_name} содержит недопустимое значение")
    if allow_zero:
        if value < 0:
            raise ValueError(f"{field_name} не может быть отрицательным")
    else:
        if value <= 0:
            raise ValueError(f"{field_name} должен быть положительным числом")
    return float(value)

def validate_positive_int(value: Any, field_name: str, allow_zero=False) -> int:
    if not isinstance(value, int):
        raise TypeError(f"{field_name} должен быть целым числом")
    if allow_zero:
        if value < 0:
            raise ValueError(f"{field_name} не может быть отрицательным")
    else:
        if value <= 0:
            raise ValueError(f"{field_name} должен быть положительным целым числом")
    return value

def validate_date(value: Any, field_name: str) -> datetime:
    if isinstance(value, datetime):
        return value
    if isinstance(value, str):
        try:
            return datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"{field_name} должен быть в формате ГГГГ-ММ-ДД")
    raise TypeError(f"{field_name} должен быть строкой или datetime")

def validate_phone(value: Any) -> str:
    return validate_string(value, "Телефон", min_len=10, max_len=20)

def validate_email(value: Any) -> str:
    value = validate_string(value, "Email", min_len=5, max_len=100)
    if '@' not in value or '.' not in value.split('@')[1]:
        raise ValueError("Некорректный формат email")
    return value