budget_for_film = float(input())
number_of_extras = int(input())
price_for_clothing_of_one_extra = float(input())

decor = budget_for_film * 0.10

if number_of_extras > 150:
    price_for_clothing_of_one_extra *= 0.90

total_expenses = decor + number_of_extras * price_for_clothing_of_one_extra

if total_expenses <= budget_for_film:
    print("Action!")
    print(f"Wingard starts filming with {budget_for_film - total_expenses:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total_expenses - budget_for_film:.2f} leva more.")