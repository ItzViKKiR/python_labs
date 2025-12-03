from models import Student
from serialize import students_to_json, students_from_json

# --- Создание объектов ---
s1 = Student("Шубкин Александр Андреевич", "2004-02-22", "БИВТ-22-01", 4.7)
s2 = Student("Гринец Петр Иванович", "2004-11-02", "БИВТ-22-02", 3.9)

print("Проверка age():", s1.age())
print("Проверка __str__():", s1)

students = [s1, s2]

# --- Сохранение в JSON ---
output_path = "Year1_Sem1/data/lab08/students_into_json.json"
students_to_json(students, output_path)

# --- Загрузка из JSON ---
input_path = "Year1_Sem1/data/lab08/students.json"
loaded_students = students_from_json(input_path)
print("Студенты, загруженные из JSON:")
for s in loaded_students:
    print(s, "| возраст:", s.age())
