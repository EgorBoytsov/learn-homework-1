"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую

"""

questions_and_answers = {}

def ask_user(answers_dict):
    questions_and_answers = {
        "Как дела?": "Хорошо!",
        "Что делаешь?": "Программирую",
        "Как здоровье?": "Здорово",
        "Сложно программировать?": "Не спрашивай",
        "Хорошей учебы!": "Пока"
    }

    while True:
        user_say = str(input('Введите свой вопрос :\n')).capitalize()

        if user_say in questions_and_answers.keys():
            print(questions_and_answers[user_say])
            if questions_and_answers[user_say] == 'Пока':
                break
        else:
            print('Не могу ответить на твой вопрос!')

if __name__ == "__main__":
    ask_user(questions_and_answers)
