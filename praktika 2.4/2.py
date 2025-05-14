import sqlite3

def create_tables():
    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS drinks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        alcohol REAL DEFAULT 0,
        volume INTEGER,
        price REAL,
        quantity INTEGER DEFAULT 0)
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        unit TEXT,
        quantity INTEGER DEFAULT 0)
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cocktails (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        alcohol REAL DEFAULT 0,
        price REAL)
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cocktail_components (
        cocktail_id INTEGER,
        component_id INTEGER,
        component_type TEXT,
        amount REAL,
        FOREIGN KEY (cocktail_id) REFERENCES cocktails(id))
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_id INTEGER,
        item_type TEXT,
        quantity INTEGER,
        total REAL)
    ''')
    conn.commit()
    conn.close()

def add_drink():
    print("\nДобавление нового напитка:")
    name = input("Название: ")
    alcohol = float(input("Крепость (%): "))
    volume = int(input("Объем (мл): "))
    price = float(input("Цена: "))
    quantity = int(input("Количество: "))
    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO drinks (name, alcohol, volume, price, quantity)
    VALUES (?, ?, ?, ?, ?)
    ''', (name, alcohol, volume, price, quantity))
    conn.commit()
    conn.close()
    print(f"Напиток '{name}' добавлен!")

def add_ingredient():
    print("\nДобавление нового ингредиента:")
    name = input("Название: ")
    unit = input("Единица измерения (г, мл, шт): ")
    quantity = int(input("Количество: "))

    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO ingredients (name, unit, quantity)
    VALUES (?, ?, ?)
    ''', (name, unit, quantity))
    conn.commit()
    conn.close()
    print(f"Ингредиент '{name}' добавлен!")

def add_cocktail():
    print("\nДобавление нового коктейля:")
    name = input("Название: ")
    price = float(input("Цена: "))

    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()
    print("\nДоступные напитки:")
    drinks = cursor.execute('SELECT id, name, alcohol FROM drinks').fetchall()
    for drink in drinks:
        print(f"{drink[0]}. {drink[1]} ({drink[2]}%)")
    print("\nДоступные ингредиенты:")
    ingredients = cursor.execute('SELECT id, name FROM ingredients').fetchall()
    for ing in ingredients:
        print(f"{ing[0]}. {ing[1]}")

    components = []
    total_alcohol = 0
    total_volume = 0

    while True:
        print("\nДобавить компонент:")
        print("1. Напиток")
        print("2. Ингредиент")
        print("0. Закончить")

        choice = input("Выберите тип компонента: ")
        if choice == '0':
            break
        elif choice == '1':
            drink_id = int(input("ID напитка: "))
            amount = float(input("Количество (мл): "))

            drink = cursor.execute('SELECT alcohol, volume FROM drinks WHERE id=?', (drink_id,)).fetchone()
            if drink:
                alcohol, volume = drink
                total_alcohol += alcohol * amount / volume
                total_volume += amount

            components.append({'type': 'drink', 'id': drink_id, 'amount': amount})
        elif choice == '2':
            ing_id = int(input("ID ингредиента: "))
            amount = float(input("Количество: "))
            components.append({'type': 'ingredient', 'id': ing_id, 'amount': amount})

    cocktail_alcohol = total_alcohol / total_volume * 100 if total_volume > 0 else 0

    cursor.execute('''
    INSERT INTO cocktails (name, alcohol, price)
    VALUES (?, ?, ?)
    ''', (name, cocktail_alcohol, price))
    cocktail_id = cursor.lastrowid
    for component in components:
        cursor.execute('''
        INSERT INTO cocktail_components (cocktail_id, component_id, component_type, amount)
        VALUES (?, ?, ?, ?)
        ''', (cocktail_id, component['id'], component['type'], component['amount']))

    conn.commit()
    conn.close()
    print(f"\nКоктейль '{name}' добавлен! Крепость: {cocktail_alcohol:.1f}%")

def sell_item():
    print("\nПродажа:")
    print("1. Напиток")
    print("2. Коктейль")
    choice = input("Выберите тип: ")
    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()

    if choice == '1':
        print("\nДоступные напитки:")
        drinks = cursor.execute('SELECT id, name, quantity, price FROM drinks').fetchall()
        for drink in drinks:
            print(f"{drink[0]}. {drink[1]} (Остаток: {drink[2]}, Цена: {drink[3]} руб.)")
        item_id = int(input("\nID напитка: "))
        quantity = int(input("Количество: "))
        item_type = 'drink'

        current = cursor.execute('SELECT quantity FROM drinks WHERE id=?', (item_id,)).fetchone()[0]
        if current < quantity:
            print("Недостаточно напитков на складе!")
            conn.close()
            return

        price = cursor.execute('SELECT price FROM drinks WHERE id=?', (item_id,)).fetchone()[0]
        cursor.execute('UPDATE drinks SET quantity = quantity - ? WHERE id = ?', (quantity, item_id))

    elif choice == '2':
        print("\nДоступные коктейли:")
        cocktails = cursor.execute('SELECT id, name, price FROM cocktails').fetchall()
        for cocktail in cocktails:
            print(f"{cocktail[0]}. {cocktail[1]} (Цена: {cocktail[2]} руб.)")

        item_id = int(input("\nID коктейля: "))
        quantity = int(input("Количество: "))
        item_type = 'cocktail'

        components = cursor.execute('''
        SELECT component_id, component_type, amount 
        FROM cocktail_components 
        WHERE cocktail_id=?
        ''', (item_id,)).fetchall()

        for comp_id, comp_type, amount in components:
            if comp_type == 'drink':
                current = cursor.execute('SELECT quantity FROM drinks WHERE id=?', (comp_id,)).fetchone()[0]
                if current < amount * quantity:
                    print("Недостаточно компонентов для коктейля!")
                    conn.close()
                    return

        for comp_id, comp_type, amount in components:
            if comp_type == 'drink':
                cursor.execute('UPDATE drinks SET quantity = quantity - ? WHERE id = ?',
                               (amount * quantity, comp_id))
            elif comp_type == 'ingredient':
                cursor.execute('UPDATE ingredients SET quantity = quantity - ? WHERE id = ?',
                               (amount * quantity, comp_id))

        price = cursor.execute('SELECT price FROM cocktails WHERE id=?', (item_id,)).fetchone()[0]

    total = price * quantity
    cursor.execute('''
    INSERT INTO sales (item_id, item_type, quantity, date, total)
    VALUES (?, ?, ?, ?)
    ''',(item_id, item_type, quantity, total))
    conn.commit()
    conn.close()
    print(f"\nПродажа оформлена. Сумма: {total:.2f} руб.")

def restock():
    print("\nПополнение запасов:")
    print("1. Напиток")
    print("2. Ингредиент")
    choice = input("Выберите тип: ")
    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()

    if choice == '1':
        print("\nДоступные напитки:")
        drinks = cursor.execute('SELECT id, name, quantity FROM drinks').fetchall()
        for drink in drinks:
            print(f"{drink[0]}. {drink[1]} (Остаток: {drink[2]})")

        item_id = int(input("\nID напитка: "))
        quantity = int(input("Количество: "))
        item_type = 'drink'
        cursor.execute('UPDATE drinks SET quantity = quantity + ? WHERE id = ?', (quantity, item_id))

    elif choice == '2':
        print("\nДоступные ингредиенты:")
        ingredients = cursor.execute('SELECT id, name, quantity FROM ingredients').fetchall()
        for ing in ingredients:
            print(f"{ing[0]}. {ing[1]} (Остаток: {ing[2]})")

        item_id = int(input("\nID ингредиента: "))
        quantity = int(input("Количество: "))
        item_type = 'ingredient'

        cursor.execute('UPDATE ingredients SET quantity = quantity + ? WHERE id = ?', (quantity, item_id))

    conn.commit()
    conn.close()
    print("\nЗапасы пополнены!")


def show_stock():
    print("\nОстатки на складе:")

    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()

    print("\nНапитки:")
    drinks = cursor.execute('SELECT name, alcohol, quantity, price FROM drinks').fetchall()
    for drink in drinks:
        print(f"{drink[0]} ({drink[1]}%) - {drink[2]} шт. по {drink[3]} руб.")

    print("\nИнгредиенты:")
    ingredients = cursor.execute('SELECT name, quantity, unit FROM ingredients').fetchall()
    for ing in ingredients:
        print(f"{ing[0]} - {ing[1]} {ing[2]}")

    print("\nКоктейли:")
    cocktails = cursor.execute('SELECT name, alcohol, price FROM cocktails').fetchall()
    for cocktail in cocktails:
        print(f"{cocktail[0]} ({cocktail[1]:.1f}%) - {cocktail[2]} руб.")
    conn.close()

def main():
    create_tables()
    while True:
        print("\n=== I Love Drink ===")
        print("1. Добавить напиток")
        print("2. Добавить ингредиент")
        print("3. Добавить коктейль")
        print("4. Продать товар")
        print("5. Пополнить запасы")
        print("6. Показать остатки")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_drink()
        elif choice == '2':
            add_ingredient()
        elif choice == '3':
            add_cocktail()
        elif choice == '4':
            sell_item()
        elif choice == '5':
            restock()
        elif choice == '6':
            show_stock()
        elif choice == '7':
                break
if __name__ == "__main__":
    main()