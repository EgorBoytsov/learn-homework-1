"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""

def string(first_str, second_str):
    if type(first_str) != str or type(second_str) != str:
        return 'Это не строка, введите число'
    if first_str == second_str:
        return 'Cтроки равны по длинне'
    if len(first_str) > len(second_str) and second_str != 'learn':
        return 'Первая строка длиннее и не равна learn'
    if first_str != second_str and second_str == 'learn':
        return 'строки по длинне не равны, но втрорая равна learn'


if __name__ == "__main__":
    print(string(1, 3))
    print(string("Python", "Python"))
    print(string("Python", "bet"))
    print(string("Python", 'learn'))
