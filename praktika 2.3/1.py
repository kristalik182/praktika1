class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days
    def get_salary(self):
        salary = self.rate * self.days
        return salary
    def display_info(self):
        print(f"Работник: {self.name} {self.surname}")
        print(f"Ставка за день: {self.rate}")
        print(f"Количество отработанных дней: {self.days}")
        print(f"Зарплата: {self.get_salary()}")
def main():
    name = input("Введите имя работника: ")
    surname = input("Введите фамилию работника: ")
    rate = float(input("Введите ставку за день работы: "))
    days = int(input("Введите количество отработанных дней: "))
    worker = Worker(name, surname, rate, days)
    worker.display_info()
if __name__ == "__main__":
    main()
