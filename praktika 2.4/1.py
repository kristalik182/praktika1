import sqlite3

class Student:
    def __init__(self, name, surname, middle_name, group, grades):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.group = group
        self.grades = grades
        if len(grades) != 4:
            raise ValueError("Успеваемость должна содержать 4 оценки")
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

class StudentDatabase:
    def __init__(self, db_name='students.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                surname TEXT,
                                middle_name TEXT,
                                groups INTEGER,
                                grades REAL)''')
        self.conn.commit()

    def add_student(self, student):
        grades_str = ','.join(map(str, student.grades))
        self.cursor.execute('''INSERT INTO students (name, surname, middle_name, groups, grades)
                               VALUES (?, ?, ?, ?, ?)''',
                            (student.name, student.surname, student.middle_name, student.group, grades_str))
        self.conn.commit()

    def get_all_students(self):
        self.cursor.execute('SELECT * FROM students')
        return self.cursor.fetchall()

    def get_student(self, student_id):
        self.cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
        return self.cursor.fetchone()

    def edit_student(self, student_id, student):
        grades_str = ','.join(map(str, student.grades))
        self.cursor.execute('''UPDATE students SET name = ?, surname = ?, middle_name = ?, groups = ?, grades = ?
                               WHERE id = ?''',
                            (student.name, student.surname, student.middle_name, student.group, grades_str,
                             student_id))
        self.conn.commit()

    def delete_student(self, student_id):
        self.cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        self.conn.commit()

    def average_grade_by_group(self, group):
        self.cursor.execute('SELECT grades FROM students WHERE groups = ?', (group,))
        grades = []
        for row in self.cursor.fetchall():
            grades.extend(map(int, row[0].split(',')))
        return sum(grades) / len(grades) if grades else 0


def main():
    db = StudentDatabase()

    while True:
        print("1. Добавление нового студента")
        print("2. Просмотр всех студентов")
        print("3. Просмотр одного студента")
        print("4. Редактирование студента")
        print("5. Удаление студента")
        print("6. Просмотр среднего балла студентов у конкретной группы")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            middle_name = input("Введите отчество: ")
            group = input("Введите группу: ")
            grades = list(map(int, input("Введите 4 оценки через запятую: ").split(',')))
            student = Student(name, surname, middle_name, group, grades)
            db.add_student(student)

        elif choice == '2':
            students = db.get_all_students()
            for student in students:
                print(student)

        elif choice == '3':
            student_id = int(input("Введите ID студента: "))
            student = db.get_student(student_id)
            if student:
                print(student)
                print("Средний балл:", Student(student[1], student[2], student[3], student[4],
                                               list(map(int, student[5].split(',')))).average_grade())
            else:
                print("Студент не найден.")

        elif choice == '4':
            student_id = int(input("Введите ID студента для редактирования: "))
            name = input("Введите новое имя: ")
            surname = input("Введите новую фамилию: ")
            middle_name = input("Введите новое отчество: ")
            group = input("Введите новую группу: ")
            grades = list(map(int, input("Введите 4 новые оценки через запятую: ").split(',')))
            student = Student(name, surname, middle_name, group, grades)
            db.edit_student(student_id, student)

        elif choice == '5':
            student_id = int(input("Введите ID студента для удаления: "))
            db.delete_student(student_id)

        elif choice == '6':
            group = input("Введите название группы: ")
            average = db.average_grade_by_group(group)
            print("Средний балл группы", group, ":", average)

        elif choice == '7':
            break

        else:
            print("Некорректный ввод. Пожалуйста, попробуйте снова.")
if __name__ == "__main__":
    main()
