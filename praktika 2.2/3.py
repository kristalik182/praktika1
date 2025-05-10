num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
class IntegerStorage:
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    def display(self):
        print(f"Число 1: {self.num1}, Число 2: {self.num2}")
    def change_numbers(self, new_num1, new_num2):
        self.num1 = new_num1
        self.num2 = new_num2
    def sum_values(self):
        return self.num1 + self.num2
    def max_value(self):
        return max(self.num1, self.num2)
if __name__ == "__main__":

    storage = IntegerStorage(num1, num2)
    storage.display()
    new_num1 = int(input("Введите новое первое число: "))
    new_num2 = int(input("Введите новое второе число: "))
    storage.change_numbers(new_num1, new_num2)
    storage.display()
    total = storage.sum_values()
    print(f"Сумма значений: {total}")
    maximum = storage.max_value()
    print(f"Наибольшее значение: {maximum}")