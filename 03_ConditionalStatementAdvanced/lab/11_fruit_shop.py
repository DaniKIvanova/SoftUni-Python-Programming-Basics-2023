fruit = input()
day_of_week = input()
quantity = float(input())

fruit_price = 0

work_banana_price = 2.50
work_apple_price = 1.20
work_orange_price = 0.85
work_grapefruit_price = 1.45
work_kiwi_price = 2.70
work_pineapple_price = 5.50
work_grapes_price = 3.85

relax_banana_price = 2.70
relax_apple_price = 1.25
relax_orange_price = 0.90
relax_grapefruit_price = 1.60
relax_kiwi_price = 3.00
relax_pineapple_price = 5.60
relax_grapes_price = 4.20

if day_of_week == "Monday" or day_of_week == "Tuesday" or \
        day_of_week == "Wednesday" or day_of_week == "Thursday" or \
        day_of_week == "Friday":
    if fruit == "banana":
        fruit_price = quantity * work_banana_price
    elif fruit == "apple":
        fruit_price = quantity * work_apple_price
    elif fruit == "grapefruit":
        fruit_price = quantity * work_grapefruit_price
    elif fruit == "kiwi":
        fruit_price = quantity * work_kiwi_price
    elif fruit == "grapes":
        fruit_price = quantity * work_grapes_price
    elif fruit == "orange":
        fruit_price = quantity * work_orange_price
    elif fruit == "pineapple":
        fruit_price = quantity * work_pineapple_price

elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        fruit_price = quantity * relax_banana_price
    elif fruit == "apple":
        fruit_price = quantity * relax_apple_price
    elif fruit == "grapefruit":
        fruit_price = quantity * relax_grapefruit_price
    elif fruit == "kiwi":
        fruit_price = quantity * relax_kiwi_price
    elif fruit == "grapes":
        fruit_price = quantity * relax_grapes_price
    elif fruit == "orange":
        fruit_price = quantity * relax_orange_price
    elif fruit == "pineapple":
        fruit_price = quantity * relax_pineapple_price

if fruit_price == 0:
    print("error")
else:
    print(f"{fruit_price:.2f}")