class MyClass:
    def __init__(self, property_one=0, property_two="default"):
        self.property_one = property_one
        self.property_two = property_two
    def __del__(self):
        print(f"Объект {self} удаляется.")
    def display(self):
        print(f"Свойство 1: {self.property_one}, Свойство 2: {self.property_two}")

def main():
    property_one_input = int(input("Введите значение для свойства 1: "))
    property_two_input = input("Введите значение для свойства 2: ")
    obj1 = MyClass(property_one_input, property_two_input)
    obj1.display()
    obj2 = MyClass()
    obj2.display()

    print("Изменяем свойства объекта 1.")
    obj1.property_one += 5
    obj1.property_two = input("Введите новое значение для свойства 2: ")
    obj1.display()
    del obj1
    del obj2
if __name__ == "__main__":
    main()