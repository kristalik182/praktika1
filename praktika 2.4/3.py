import psutil
import sqlite3
from datetime import datetime

def connect_date_base():
    return sqlite3.connect('system_monitor.db')

def create_tables():
    connect = connect_date_base()
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS MonitoringData (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp DATETIME NOT NULL,
                        cpu_usage REAL NOT NULL,
                        memory_usage REAL NOT NULL,
                        disk_usage REAL NOT NULL)''')
    connect.commit()
    connect.close()

def save_monitoring_data(cpu, memory, disk):
    connect = connect_date_base()
    cursor = connect.cursor()
    cursor.execute("INSERT INTO MonitoringData (timestamp, cpu_usage, memory_usage, disk_usage) VALUES (?, ?, ?, ?)",
                   (datetime.now(), cpu, memory, disk))
    connect.commit()
    connect.close()

def show_monitoring_data():
    connect = connect_date_base()
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM MonitoringData")
    rows = cursor.fetchall()
    print("Сохраненные данные мониторинга:")
    for row in rows:
        print(f"Время: {row[1]}, CPU: {row[2]}%, RAM: {row[3]}%, Disk: {row[4]}%")
    connect.close()

def main():
    create_tables()
    while True:
        print("1 - Мониторинг системных ресурсов\n"
              "2 - Показать сохраненные данные\n"
              "3 - Выход")
        choice = int(input("Выберите действие: "))
        if choice == 1:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_usage = psutil.virtual_memory().percent
            disk_usage = psutil.disk_usage('/').percent

            save_monitoring_data(cpu_usage, memory_usage, disk_usage)
            print(f"Данные сохранены: CPU - {cpu_usage}%, RAM - {memory_usage}%, Disk - {disk_usage}%")
        elif choice == 2:
            show_monitoring_data()
        elif choice == 3:
            print("Выход из приложения.")
            break
        else:
            print("Некорректный ввод!")
if __name__ == "__main__":
    main()