import json
from pathlib import Path

from models import RentalProperty, MortgageProperty


BASE_DIR = Path(__file__).resolve().parent
TEST_FOLDER = BASE_DIR / "test_files"


def save(collection, filepath: str) -> None:

    TEST_FOLDER.mkdir(exist_ok=True)

    full_path = TEST_FOLDER / filepath

    data = []

    for item in collection.get_all():

        if isinstance(item, RentalProperty):
            data.append({
                "type": "rental",
                "owner": item.owner,
                "price": item.price,
                "rent_term": item.rent_term,
                "utilities": item.utilities,
                "mortgage": item.mortgage
            })

        elif isinstance(item, MortgageProperty):
            data.append({
                "type": "mortgage",
                "owner": item.owner,
                "price": item.price,
                "rent_term": item.rent_term,
                "utilities": item.utilities,
                "mortgage": item.mortgage,
                "rate": item._rate,
                "years": item._years
            })

    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load(filename: str) -> list:

    path = TEST_FOLDER / filename

    if not path.exists():
        return []

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)


    items = []

    for item in data:

        if item["type"] == "rental":
            items.append(RentalProperty(
                item["owner"],
                item["price"],
                item["rent_term"],
                item["utilities"],
                item["mortgage"]
            ))

        elif item["type"] == "mortgage":
            items.append(MortgageProperty(
                item["owner"],
                item["price"],
                item["rent_term"],
                item["utilities"],
                item["mortgage"],
                item["rate"],
                item["years"]
            ))

    return items