# Задача 2.1

arr = [4, 6, 2, 1, 9, 63, -134, 566]
       


def minimum(arr):
 result = float()
 for num in arr:
   if num < result:
    result = num
    return result
def maximum(arr):
 result = float()
 for num in arr:
   if num > result:
    result = num
 return result
print('min =', minimum(arr), 'max =', maximum(arr)) 


# Задача 2.2
def квартал(month):
    if month in [1, 2, 3]:
        return '1 квартал'
    elif month in [4, 5, 6]:
        return '2 квартал'
    elif month in [7, 8, 9]:
        return '3 квартал'
    elif month in [10, 11, 12]:
        return '4 квартал'

month = int(input("Введите номер месяца: "))
print(квартал(month))

# Задача 2.3

def switch_it_up(number):
    nums = {
        1: "один", 
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять", 
        0: "ноль"
    }
    return nums[number]
number = int(input("Введите число: "))
print(switch_it_up(number))



# Задача 2.4.1

import re   
inp_str = "Hi! Hello!"

marks = "!"
for x in inp_str:  
    if x in marks:  
        opt_str = inp_str.replace(x, "")
print(opt_str)

# Задача 2.4.2

Str = "Hi!!!"
l = len(Str)

Remove_last = Str[:l-1]

print(Remove_last)



