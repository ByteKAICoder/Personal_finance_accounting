import json
import os
import csv
from datetime import datetime


def get_file_path():
    file_path = input('Введите путь до файла для загрузки заказов ("Enter" - значение по умолчанию): ').strip()
    if not file_path:
        file_path = 'My_expenses.json'
    return file_path


def loading_data(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                orders = json.load(file)
                if orders:
                    return orders
                print('Файл пуст! Список заказов по умолчанию пуст.')
                return []
        except json.JSONDecodeError:
            print('Ошибка чтения JSON. Файл поврежден. Создан новый список.')
            return []
    print('Файл не найден. Список заказов по умолчанию пуст.')
    return []


def save_data(data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def add_expense(expenses):
    try:
        summa = float(input("Введите сумму: "))
        category = input("Введите категорию: ")
        date = input("Введите дату (ГГГГ-ММ-ДД) или нажмите Enter для текущей: ")
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")

        expenses.append({"summa": summa, "category": category, "date": date})
        save_data(expenses)
        print("Запись добавлена!")
    except ValueError:
        print("Ошибка: некорректное число.")


def show_expenses(expenses, filter_val=None, filter_type=None):
    if filter_type == 'category':
        filtered = [i for i in expenses if i['category'].lower() == filter_val.lower()]
    elif filter_type == 'date':
        filtered = [i for i in expenses if i['date'] == filter_val]
    else:
        filtered = expenses

    if not filtered:
        print("Записей не найдено.")
        return

    print("№ | Дата | Категория | Сумма")
    print("-" * 35)

    total = 0
    for n, i in enumerate(filtered, 1):
        print(f"{n}. {i['date']} | {i['category']} | {i['summa']} руб.")
        total += i['summa']

    print("-" * 35)
    print(f"Итого: {total} руб.")


def delete_expense(expenses):
    if not expenses:
        print("Список пуст, нечего удалять.")
        return
    show_expenses(expenses)
    try:
        num = int(input("Введите номер записи для удаления: ")) - 1
        if 0 <= num < len(expenses):
            removed = expenses.pop(num)
            save_data(expenses)
            print(f"Запись '{removed['category']} на {removed['summa']} руб.' удалена.")
        else:
            print("Ошибка: записи с таким номером нет.")
    except ValueError:
        print("Ошибка: некорректное число.")


def show_stats(expenses):
    if not expenses:
        print("Нет данных для статистики.")
        return

    total_all = sum(i['summa'] for i in expenses)
    stats = {}
    for i in expenses:
        category = i['category']
        stats[category] = stats.get(category, 0) + i['summa']

    print("\nСтатистика по категориям:")
    for category, summa in stats.items():
        percent = (summa / total_all) * 100
        print(f"- {category}: {summa} руб. ({percent:.1f}%)")
    print(f"\nОбщая сумма всех расходов: {total_all} руб.")
