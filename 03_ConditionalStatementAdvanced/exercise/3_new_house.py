kind_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())

ROSE_PRICE = 5
DAHLIA_PRICE = 3.80
TULIP_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

total_price = 0

if kind_of_flowers == "Roses":
    total_price = number_of_flowers * ROSE_PRICE
    if number_of_flowers > 80:
        total_price *= 0.90
elif kind_of_flowers == "Dahlias":
    total_price = number_of_flowers * DAHLIA_PRICE
    if number_of_flowers > 90:
        total_price *= 0.85
elif kind_of_flowers == "Tulips":
    total_price = number_of_flowers * TULIP_PRICE
    if number_of_flowers > 80:
        total_price *= 0.85
elif kind_of_flowers == "Narcissus":
    total_price = number_of_flowers * NARCISSUS_PRICE
    if number_of_flowers < 120:
        total_price *= 1.15
elif kind_of_flowers == "Gladiolus":
    total_price = number_of_flowers * GLADIOLUS_PRICE
    if number_of_flowers < 80:
        total_price *= 1.20

if total_price <= budget:
    print(f"Hey, you have a great garden with {number_of_flowers} {kind_of_flowers} "
          f"and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")