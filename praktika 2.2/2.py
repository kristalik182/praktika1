class Train:
    def __init__(self, destination_point, train_number, departure_time):
        self.destination_point = destination_point
        self.train_number = train_number
        self.departure_time = departure_time

    def display_info(self):
        return f"Пункт назначения: {self.destination_point}, Номер поезда: {self.train_number}, Время отправления: {self.departure_time}"

def main():
    trains = []
    n = int(input("Введите количество поездов: "))
    for i in range(n):
        print(f"\nВведите данные для поезда {i+1}")
        destination_point = input("Пункт назначения: ")
        train_number = input("Номер поезда: ")
        departure_time = input("Время отправления: ")
        trains.append(Train(destination_point, train_number, departure_time))

    search_number = input("\nВведите номер поезда для получения информации: ")
    found = False
    for train in trains:
        if train.train_number == search_number:
            print("\nИнформация о найденном поезде:")
            print(train.display_info())
            found = True
            break
    if not found:
        print("Поезд с таким номером не найден.")
if __name__ == "__main__":
    main()
