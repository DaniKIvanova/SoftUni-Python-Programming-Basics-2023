days_to_stay = int(input())
type_of_room = input()
evaluation = input()

room_price = 18.00
apartment_price = 25.00
president_price = 35.00

overnight_stays = days_to_stay - 1
price = 0

if type_of_room == "room for one person":
    price = overnight_stays * room_price

elif type_of_room == "apartment":
    if days_to_stay < 10:
        price = (overnight_stays * apartment_price) * 0.70
    elif 10 <= days_to_stay <= 15:
        price = (overnight_stays * apartment_price) * 0.65
    elif days_to_stay > 15:
        price = (overnight_stays * apartment_price) * 0.50

elif type_of_room == "president apartment":
    if days_to_stay < 10:
        price = (overnight_stays * president_price) * 0.90
    elif 10 <= days_to_stay <= 15:
        price = (overnight_stays * president_price) * 0.85
    elif days_to_stay > 15:
        price = (overnight_stays * president_price) * 0.80

if evaluation == "positive":
    price *= 1.25
elif evaluation == "negative":
    price *= 0.90

print(f"{price:.2f}")