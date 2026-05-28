# Тема: Робота зі словниками
# Програма працює зі словником.
# Дані зберігаються у файлі students.json.
# Якщо файлу немає, створюється початковий словник.

import json
import os

FILE_NAME = "students.json"


# Початковий словник
default_students = {
    "1": {
        "group": "КНд-41с",
        "full_name": "Корпало Ярослав Андрійович",
        "course": 1,
        "subjects": {
            "Програмування": 90,
            "Математика": 85,
            "Іноземна мова": 88,
            "Історія України": 92,
            "Фізика": 80
        }
    }
}

# Завантаження словника з файлу
def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Помилка читання файлу. Буде використано початковий словник.")
            return default_students
    else:
        return default_students

# Збереження словника у файл
def save_students():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)


students = load_students()

# Виведення всіх даних словника
def print_students():
    print("\nСписок студентів:")

    if len(students) == 0:
        print("Словник порожній.")
        return

    for student_id, data in students.items():
        print("\nНомер студента:", student_id)
        print("Група:", data["group"])
        print("ПІБ:", data["full_name"])
        print("Курс:", data["course"])
        print("Предмети та оцінки:")

        for subject, grade in data["subjects"].items():
            print(" ", subject, "-", grade)


# Додавання нового студента до словника
def add_student():
    try:
        student_id = input("Введіть номер студента: ")

        if student_id in students:
            print("Студент з таким номером вже існує.")
            return

        group = input("Введіть номер групи: ")
        full_name = input("Введіть ПІБ студента: ")
        course = int(input("Введіть курс: "))

        subjects = {}
        count = int(input("Скільки предметів потрібно додати? "))

        for i in range(count):
            subject = input("Введіть назву предмета: ")
            grade = int(input("Введіть оцінку за предмет: "))

            if grade < 0 or grade > 100:
                print("Оцінка має бути від 0 до 100.")
                return

            subjects[subject] = grade

        students[student_id] = {
            "group": group,
            "full_name": full_name,
            "course": course,
            "subjects": subjects
        }

        save_students()
        print("Студента додано і збережено у файл.")

    except ValueError:
        print("Помилка введення. Курс, кількість предметів і оцінки мають бути числами.")


# Видалення студента зі словника
def delete_student():
    student_id = input("Введіть номер студента для видалення: ")

    if student_id in students:
        del students[student_id]
        save_students()
        print("Студента видалено і зміни збережено.")
    else:
        print("Студента з таким номером немає у словнику.")

# Перегляд словника за відсортованими ключами
def print_sorted_students():
    print("\nСловник, відсортований за ключами:")

    for student_id in sorted(students.keys()):
        data = students[student_id]

        print("\nНомер студента:", student_id)
        print("Група:", data["group"])
        print("ПІБ:", data["full_name"])
        print("Курс:", data["course"])
        print("Предмети та оцінки:")

        for subject, grade in data["subjects"].items():
            print(" ", subject, "-", grade)


# Обчислення середнього бала студента
def average_grade():
    student_id = input("Введіть номер студента: ")

    if student_id not in students:
        print("Студента з таким номером немає у словнику.")
        return

    grades = students[student_id]["subjects"].values()

    if len(grades) == 0:
        print("У студента немає оцінок.")
        return

    average = sum(grades) / len(grades)

    print("ПІБ:", students[student_id]["full_name"])
    print("Середній бал:", round(average, 2))


# Пошук найвищої оцінки студента
def max_grade():
    student_id = input("Введіть номер студента: ")

    if student_id not in students:
        print("Студента з таким номером немає у словнику.")
        return

    subjects = students[student_id]["subjects"]

    if len(subjects) == 0:
        print("У студента немає оцінок.")
        return

    max_subject = max(subjects, key=subjects.get)
    max_value = subjects[max_subject]

    print("ПІБ:", students[student_id]["full_name"])
    print("Найвища оцінка:", max_value)
    print("Предмет:", max_subject)


# Сортування студентів за середнім балом
def sort_by_average_grade():
    if len(students) == 0:
        print("Словник порожній.")
        return

    averages = {}

    for student_id, data in students.items():
        grades = data["subjects"].values()

        if len(grades) > 0:
            averages[student_id] = sum(grades) / len(grades)
        else:
            averages[student_id] = 0

    sorted_ids = sorted(averages, key=averages.get, reverse=True)

    print("\nСтуденти, відсортовані за середнім балом:")

    for student_id in sorted_ids:
        print(
            students[student_id]["full_name"],
            "- середній бал:",
            round(averages[student_id], 2)
        )


# Меню програми
def menu():
    while True:
        print("\nМеню")
        print("1 - Вивести всіх студентів")
        print("2 - Додати студента")
        print("3 - Видалити студента")
        print("4 - Вивести словник за відсортованими ключами")
        print("5 - Обчислити середній бал студента")
        print("6 - Знайти найвищу оцінку студента")
        print("7 - Сортувати студентів за середнім балом")
        print("0 - Вийти з програми")

        choice = input("Виберіть пункт меню: ")

        if choice == "1":
            print_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print_sorted_students()
        elif choice == "5":
            average_grade()
        elif choice == "6":
            max_grade()
        elif choice == "7":
            sort_by_average_grade()
        elif choice == "0":
            save_students()
            print("Дані збережено. Роботу програми завершено.")
            break
        else:
            print("Помилка. Такого пункту меню немає.")


menu()
