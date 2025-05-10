class Counter:
    def __init__(self, initial_value=0):
        self._value = initial_value
    def increment(self):
        self._value += 1
    def decrement(self):
        self._value -= 1
    @property
    def current_value(self):
        return self._value

def main():
    try:
        initial_input = input("Введите начальное значение счетчика (по умолчанию 0): ")
        initial_value = int(initial_input) if initial_input else 0
    except ValueError:
        print("Некорректный ввод. Устанавливаем значение по умолчанию (0).")
        initial_value = 0
    counter = Counter(initial_value)

    while True:
        print(f"Текущая значение счетчика: {counter.current_value}")
        action = input("Введите 'a' для увеличения, 'b' для уменьшения, 'c' для выхода: ").lower()
        if action == 'a':
            counter.increment()
            print("Счетчик увеличен на 1.")
        elif action == 'b':
            counter.decrement()
            print("Счетчик уменьшен на 1.")
        elif action == 'c':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз.")
if __name__ == "__main__":
    main()