from pathlib import Path
import json
import csv

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте.
    """
    json_file = Path(json_path)
    csv_file = Path(csv_path)
    if not json_file.exists():
        raise FileNotFoundError("Файл не найден")
    with json_file.open('r', encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json_file.JSONDecodeError:
            raise ValueError("Некорректный JSON-файл")
    if not isinstance(data, list) or not all(isinstance(value, dict) for value in data):
        raise ValueError("Ожидается список словарей")
    if not data:
        raise ValueError("Пустой JSON-файл")
    header = list(data[0].keys())
    with csv_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()

        for row in data:
            writer.writerow({k: row.get(k, "") for k in header})

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    """
    csv_file = Path(csv_path)
    json_file = Path(json_path)

    if not csv_file.exists():
        raise FileNotFoundError("Файл не найден")

    with csv_file.open(encoding="utf-8") as f:
        reader = csv_file.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV не содержит заголовок")
        data = [row for row in reader]

    if not data:
        raise ValueError("Пустой CSV")

    with json_file.open("w", encoding="utf-8") as f:
        json_file.dump(data, f, ensure_ascii=False, indent=2)