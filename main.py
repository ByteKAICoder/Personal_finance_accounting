import json
import os
import csv
from datetime import datetime

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
