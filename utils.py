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
