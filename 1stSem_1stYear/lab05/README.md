# Лабораторная работа №4
### Задание А
``` python
from pathlib import Path
import json
import csv

def ensure_relative(path: Path) -> None:
    if path.is_absolute():
        raise ValueError("Путь должен быть относительным")

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте.
    """
    json_file = Path(json_path)
    csv_file = Path(csv_path)
    ensure_relative(json_file)
    ensure_relative(csv_file)
    if json_file.suffix.lower() != ".json":
        raise ValueError(f"Неверный формат входного файла: ожидается .json")
    if csv_file.suffix.lower() != ".csv":
        raise ValueError(f"Неверный формат выходного файла: ожидается .csv")
    if not json_file.exists():
        raise FileNotFoundError("Файл не найден")
    with json_file.open('r', encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
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
    ensure_relative(json_file)
    ensure_relative(csv_file)
    if json_file.suffix.lower() != ".json":
        raise ValueError(f"Неверный формат выходного файла: ожидается .json")
    if csv_file.suffix.lower() != ".csv":
        raise ValueError(f"Неверный формат входного файла: ожидается .csv")
    if not csv_file.exists():
        raise FileNotFoundError("Файл не найден")
    with csv_file.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV не содержит заголовок")
        data = [row for row in reader]
        
    if not data:
        raise ValueError("Пустой CSV")
    with json_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
```
### Сценарии:
Успешная конвертация

![json to csv](/1stSem_1stYear/lab05/images/suscontocsv.png)
![csv to json](/1stSem_1stYear/lab05/images/suscontojson.png)

Ошибка при отсутствия файла
![filenotfound](/1stSem_1stYear/lab05/images/filenotfound.png)

Ошибка при неправильном входном/выходном файле
![valueerror](/1stSem_1stYear/lab05/images/valueerror.png)
### Задание B
``` python
from pathlib import Path
import csv
from openpyxl import Workbook


def ensure_relative(path: Path) -> None:
    if path.is_absolute():
        raise ValueError("Путь должен быть относительным")


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использует openpyxl. Автоматическая ширина колонок.
    """
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)
    ensure_relative(csv_file)
    ensure_relative(xlsx_file)
    if csv_file.suffix.lower() != ".csv":
        raise ValueError("Неверный формат входного файла: ожидается .csv")
    if xlsx_file.suffix.lower() != ".xlsx":
        raise ValueError("Неверный формат выходного файла: ожидается .xlsx")
    if not csv_file.exists():
        raise FileNotFoundError("Файл не найден")

    with csv_file.open(encoding="utf-8") as f:
        reader = list(csv.reader(f))
        if not reader:
            raise ValueError("Пустой файл")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in reader:
        ws.append(row)

    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter
        for cell in col:
            value = str(cell.value) if cell.value is not None else ""
            if len(value) > max_length:
                max_length = len(value)
        adjusted_width = max(max_length + 2, 8)
        ws.column_dimensions[column].width = adjusted_width

    wb.save(xlsx_file)
```
Пример результата работы:

![xlsx](/1stSem_1stYear/lab05/images/csvtoxlsx.png)