class Worker:
    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days
    def __getattr__(self, item):
        if item == "name":
            return self.__name
        elif item == "surname":
            return self.__surname
        elif item == "rate":
            return self.__rate
        elif item == "days":
            return self.__days
        raise AttributeError(f"{item} not found")
    def get_salary(self):
        salary = self.__rate * self.__days
        return salary

    def display_info(self):
        print(f"Работник: {self.name}, {self.surname}")
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
