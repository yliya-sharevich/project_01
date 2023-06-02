# Задача 2.1

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

print(switch_it_up(number))


# Задача 2.4

s = "Hi! Hello!"

def remove_exclamation_marks(s):
 return s.replace("!", "")



