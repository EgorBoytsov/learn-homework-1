"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    stoke = [
    {'product': 'iPhone 12',
    'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186, 1234]},
    {'product': 'Xiaomi Mi11',
    'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316, 3211]},
    {'product': 'Samsung Galaxy 21',
    'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247, 2341]},
  ]
    total_summ = 0
    for phone in stoke:
        phone_name = phone['product']
        summ_product = sum(phone['items_sold'])
        list_length = len(phone['items_sold'])
        avg_summ_product = round(summ_product / list_length, 2)
        total_summ += summ_product
        avg_summ = round(total_summ / list_length, 2)
        print(f'Суммарное кол-во продаж {phone_name} : {summ_product}')
        print(f'Среднее кол-во продаж {phone_name} : {avg_summ_product}')

    print(f'Суммарное кол-во продаж всех товаров : {total_summ}')
    print(f'Среднее кол-во продаж всех товаров : {avg_summ}')


if __name__ == "__main__":
    main()
