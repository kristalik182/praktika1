class Calculation:
    def __init__(self):
        self.calculationLine = ""
    def setCalculationLine(self, value):
        self.calculationLine = value
    def setLastSymbolCalculationLine(self, symbol):
        self.calculationLine += symbol
    def getCalculationLine(self):
        return self.calculationLine
    def getLastSymbol(self):
        if self.calculationLine:
            return self.calculationLine[-1]
        return None
    def deleteLastSymbol(self):
        if self.calculationLine:
            self.calculationLine = self.calculationLine[:-1]

def main():
    calc = Calculation()
    while True:
        print("\nВыберите действие:")
        print("1. Установить строку расчёта")
        print("2. Добавить символ к строке расчёта")
        print("3. Получить строку расчёта")
        print("4. Получить последний символ")
        print("5. Удалить последний символ")
        print("6. Выход")

        choice = input("Введите номер действия: ")
        if choice == "1":
            value = input("Введите новую строку расчёта: ")
            calc.setCalculationLine(value)
        elif choice == "2":
            symbol = input("Введите символ для добавления: ")
            calc.setLastSymbolCalculationLine(symbol)
        elif choice == "3":
            print(f"Строка расчёта: {calc.getCalculationLine()}")
        elif choice == "4":
            last_symbol = calc.getLastSymbol()
            if last_symbol:
                print(f"Последний символ: {last_symbol}")
            else:
                print("Строка расчёта пуста.")
        elif choice == "5":
            calc.deleteLastSymbol()
            print("Последний символ удалён.")
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод, попробуйте снова.")
if __name__ == "__main__":
    main()
