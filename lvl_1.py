# Задача 1

my_favorite_songs  =  'Упусти момент', 'останься в живых' , 'своего рода сказка', 'заведи меня', 'новое спасение'

print(my_favorite_songs[0], my_favorite_songs[-1], my_favorite_songs[1], my_favorite_songs[-2])

# Задача 2.1

import random

my_favorite_songs  = [
    [ 'Потеряй момент' , 3.03 ],
    [ 'Новое спасение' , 4.02 ],
    [ ' Остаться в живых' , 3.40 ],
    [ 'Вне связи' , 3.03 ],
    [ 'Эта сказка' , 5.28 ],
    [ 'Легко' , 4.15 ],
    [ 'Прекрасный день' , 4.04 ],
    [ 'Некуда бежать' , 2.58 ],
    [ 'В этом мире' , 4.02 ],
]

x = (random.sample(my_favorite_songs, 3))

total_minutes = 0
for i in x:
  total_minutes += i[1]

print(f'Три песни звучат {total_minutes} минут')

# Задача 2.2

from random import sample

my_favorite_songs  = {
     'Потеряй момент': 3.03 ,
     'Новое спасение': 4.02 ,
     ' Остаться в живых': 3.40 ,
     'Вне связи': 3.03 ,
     'Эта сказка': 5.28 ,
     'Легко': 4.15 ,
     'Прекрасный день': 4.04 ,
     'Некуда бежать': 2.58 ,
     'В этом мире': 4.02 ,
}

x = list(my_favorite_songs.items())
y = sample(x, 3)

total_minutes = 0
for i in y:
  total_minutes += i[1]

print(f'Три песни звучат {total_minutes} минут')

# Задача 3

user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
month_number = {
    1: 31,
    3: 31,
    2: 28,
    5: 31,
    4: 30,
    6: 30,
    8: 30,
    7: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

if month in month_number:
    print('В этом месяце', month_number[month], 'дней')

else:
    print("Такого номера месяца нет в году")
    print('Введите число от 1 до 12')

# Задача 4

goods = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}



for title, code in goods.items(): 
    total_quantity = 0  
    total_cost = 0  
    for goods in store[code]:
        total_quantity += goods['quantity']
        total_cost += goods['price'] * goods['quantity']

    print(title, " - ", total_quantity, " шт, ", 'стоимость', total_cost, " руб")