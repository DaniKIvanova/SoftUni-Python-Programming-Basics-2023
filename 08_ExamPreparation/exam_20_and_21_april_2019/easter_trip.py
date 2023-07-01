destination = input()
dates_excursion = input()
number_of_nights = int(input())

price_of_night = 0

if destination == "France":
    if dates_excursion == "21-23":
        price_of_night = 30
    elif dates_excursion == "24-27":
        price_of_night = 35
    elif dates_excursion == "28-31":
        price_of_night = 40
elif destination == "Italy":
    if dates_excursion == "21-23":
        price_of_night = 28
    elif dates_excursion == "24-27":
        price_of_night = 32
    elif dates_excursion == "28-31":
        price_of_night = 39
elif destination == "Germany":
    if dates_excursion == "21-23":
        price_of_night = 32
    elif dates_excursion == "24-27":
        price_of_night = 37
    elif dates_excursion == "28-31":
        price_of_night = 43

total_cost = number_of_nights * price_of_night

print(f"Easter trip to {destination} : {total_cost:.2f} leva.")