number_of_eggs_painted = int(input())

number_red_eggs = 0
number_orange_eggs = 0
number_blue_eggs = 0
number_green_eggs = 0
max_eggs_number_from_color = 0

for _ in range(number_of_eggs_painted):
    egg_color = input()
    if egg_color == "red":
        number_red_eggs += 1
    elif egg_color == "orange":
        number_orange_eggs += 1
    elif egg_color == "blue":
        number_blue_eggs += 1
    elif egg_color == "green":
        number_green_eggs += 1

if number_blue_eggs < number_red_eggs > number_orange_eggs and number_red_eggs > number_green_eggs:
    color = "red"
    max_eggs_number_from_color = number_red_eggs

elif number_blue_eggs < number_orange_eggs > number_red_eggs and number_orange_eggs > number_green_eggs:
    color = "orange"
    max_eggs_number_from_color = number_orange_eggs

elif number_orange_eggs < number_blue_eggs > number_red_eggs and number_blue_eggs > number_green_eggs:
    color = "blue"
    max_eggs_number_from_color = number_blue_eggs
else:
    color = "green"
    max_eggs_number_from_color = number_green_eggs

print(f"Red eggs: {number_red_eggs}")
print(f"Orange eggs: {number_orange_eggs}")
print(f"Blue eggs: {number_blue_eggs}")
print(f"Green eggs: {number_green_eggs}")
print(f"Max eggs: {max_eggs_number_from_color} -> {color}")