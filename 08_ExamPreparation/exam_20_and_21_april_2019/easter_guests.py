import math

number_of_guests = int(input())
budget = int(input())

one_easter_bread = 4
one_egg = 0.45

number_of_easter_bread = math.ceil(number_of_guests / 3)
number_of_eggs = number_of_guests * 2
price_easter_breads = number_of_easter_bread * one_easter_bread
price_eggs = number_of_eggs * 0.45
total_price = price_easter_breads + price_eggs

if total_price <= budget:
    print(f"Lyubo bought {number_of_easter_bread} Easter bread and {number_of_eggs} eggs.")
    print(f"He has {budget - total_price:.2f} lv. left.")
elif total_price > budget:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {total_price - budget:.2f} lv. more.")