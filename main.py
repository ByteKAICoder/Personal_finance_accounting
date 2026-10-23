from utils import *

def main():
    print('-' * 40)
    print('\nУЧЁТ ЛИЧНЫХ РАСХОДОВ\n')
    print('-' * 40)

    while True:
        print('\nМЕНЮ ПРИЛОЖЕНИЯ:\n')
        print('-' * 40)
        print('1. Добавить расход')
        print('2. Все записи')
        print('3. Фильтр по категории')
        print('4. Фильтр по дате')
        print('5. Удалить запись')
        print('6. Статистика и общая сумма')
        print('7. Выход')
        print('-' * 40)
        
        choice = input_validation(1, 7, '\nВведите номер пункта меню: ')

        match choice:
            case 1:
                add_expense(expenses)
            case 2:
                show_expenses(expenses)
            case 3:
                categorys = set(f'- {i['category']}' for i in expenses)
                if categorys:
                    print("Доступные категории:")
                    print(*categorys, sep = '\n')
                category = input("Категория для фильтра: ")
                show_expenses(expenses, category, 'category')
            case 4:
                dates = set(f'- {i['date']}' for i in expenses)
                if dates:
                    print("Доступные даты:")
                    print(*dates, sep = '\n')
                date = input("Введите дату (ГГГГ-ММ-ДД): ")
                show_expenses(expenses, date, 'date')
            case 5:
                delete_expense(expenses)
            case 6:
                show_stats(expenses)
            case 7:
                print('Вы вышли из приложения! До свидания!')
                break


if __name__ == '__main__':
    main()
