group_budget = int(input())
season = input()
number_of_fishermen = int(input())

total_price = 0

if season == "Spring":
    total_price = 3000
elif season == "Winter":
    total_price = 2600
else:
    total_price = 4200

if number_of_fishermen <= 6:
    total_price *= 0.90
elif 7 <= number_of_fishermen <= 11:
    total_price *= 0.85
else:
    total_price *= 0.75

if number_of_fishermen % 2 == 0 and season != "Autumn":
    total_price *= 0.95

if total_price <= group_budget:
    print(f"Yes! You have {group_budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_price - group_budget:.2f} leva.")