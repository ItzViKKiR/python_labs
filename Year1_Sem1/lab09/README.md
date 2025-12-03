# Лабораторная работа №9
### Класс Group
``` python
import csv
from pathlib import Path
from models import Student


class Group:
    HEADER = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        if not self.path.exists():
            with self.path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(self.HEADER)

    def _read_all(self):
        students = []
        with self.path.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(
                    Student(
                        fio=row["fio"],
                        birthdate=row["birthdate"],
                        group=row["group"],
                        gpa=float(row["gpa"]),
                    )
                )
        return students

    def list(self):
        return self._read_all()

    def add(self, student):
        with self.path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                [student.fio, student.birthdate, student.group, student.gpa]
            )

    def find(self, substr):
        substr = substr.lower()
        return [s for s in self._read_all() if substr in s.fio.lower()]

    def remove(self, fio):
        students = self._read_all()
        students = [s for s in students if s.fio != fio]

        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(self.HEADER)
            for s in students:
                writer.writerow([s.fio, s.birthdate, s.group, s.gpa])

    def update(self, fio: str, **fields):
        students = self._read_all()

        for s in students:
            if s.fio == fio:

                if "fio" in fields:
                    s.fio = fields["fio"]

                if "birthdate" in fields:
                    s.birthdate = fields["birthdate"]

                if "group" in fields:
                    s.group = fields["group"]

                if "gpa" in fields:
                    s.gpa = fields["gpa"]

            break

        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(self.HEADER)
            for st in students:
                writer.writerow([st.fio, st.birthdate, st.group, st.gpa])
                break

            with self.path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(self.HEADER)
                for s in students:
                    writer.writerow([s.fio, s.birthdate, s.group, s.gpa])

```
CSV до всех тестов:
![basiccsv](/Year1_Sem1/lab09/images/basecsv.png)

Тесты:
![testresults](/Year1_Sem1/lab09/images/tests.png)

CSV после всех тестов:
![endcsv](/Year1_Sem1/lab09/images/endcsv.png)