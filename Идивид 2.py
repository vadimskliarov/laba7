#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import sys

if __name__ == '__main__':
    market = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о человеке.
            name = input("Имя? ")
            name1 = input("Фамилия? ")
            phone = float(input("Номер телефона? "))
            day = input("День рождения? ")


            # Создать словарь.
            markets = {
                'name': name,
                'name1': name1,
                'phone': phone,
                'day': day,
            }
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                ' | {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                    "Имя",
                    "Фамилия",
                    "Номер телефона",
                    "День рождения"
                )
            )

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить человека;")
            print("select - ;")
            print("list - вывести список людей;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")


        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
