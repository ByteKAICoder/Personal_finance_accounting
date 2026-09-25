def get_file_path():
    file_path = input('Введите путь до файла для загрузки заказов ("Enter" - значение по умолчанию): ').strip()
    if not file_path:
        file_path = 'My_expenses.json'
    return file_path
