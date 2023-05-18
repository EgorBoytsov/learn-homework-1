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
        return '0'
    if first_str == second_str:
        return '1'
    if len(first_str) > len(second_str) and second_str != 'learn':
        return '2'
    if first_str != second_str and second_str == 'learn':
        return '3'


if __name__ == "__main__":
    print(string(1, 3))
    print(string("Python", "Python"))
    print(string("Python", "bet"))
    print(string("Python", 'learn'))
