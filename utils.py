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
