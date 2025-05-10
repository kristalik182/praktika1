class Student:
    def __init__(self, surname, birth_date, group_number, grades):
        self.surname = surname
        self.birth_date = birth_date
        self.group_number = group_number
        self.grades = grades

    def change_surname(self, new_surname):
        self.surname = new_surname
    def change_birth_date(self, new_birth_date):
        self.birth_date = new_birth_date
    def change_group_number(self, new_group_number):
        self.group_number = new_group_number
    def display_info(self):
        return f"Фамилия: {self.surname}, Дата рождения: {self.birth_date}, Номер группы: {self.group_number}, Успеваемость: {self.grades}"

def main():
    surname = input("Введите фамилию студента: ")
    birth_date = input("Введите дату рождения студента: ")
    group_number = input("Введите номер группы студента: ")
    grades = [float(input(f"Введите оценку {i + 1}: ")) for i in range(5)]

    student = Student(surname, birth_date, group_number, grades)
    print("\nИнформация о студенте:")
    print(student.display_info())
    change_info = input("\nХотите изменить данные студента? (да/нет): ").strip().lower()

    while change_info == 'да':
        print("\nЧто вы хотите изменить?")
        print("1. Фамилия")
        print("2. Дата рождения")
        print("3. Номер группы")
        choice = int(input("Выберите номер изменения: "))

        if choice == 1:
            new_surname = input("Введите новую фамилию: ")
            student.change_surname(new_surname)
        elif choice == 2:
            new_birth_date = input("Введите новую дату рождения: ")
            student.change_birth_date(new_birth_date)
        elif choice == 3:
            new_group_number = input("Введите новый номер группы: ")
            student.change_group_number(new_group_number)

        print("\nОбновлённая информация о студенте:")
        print(student.display_info())
        change_info = input("\nХотите изменить ещё что-то? (да/нет): ").strip().lower()
if __name__ == "__main__":
    main()
