month = input()
number_nights = int(input())

studio_price = 0
apartment_price = 0
studio_discount = 1
apartment_discount = 1

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65

    if 7 < number_nights <= 14:
        studio_discount = 0.95

    if number_nights > 14:
        studio_discount = 0.70

elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70

    if number_nights > 14:
        studio_discount *= 0.80

elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77

if number_nights > 14:
    apartment_discount = 0.90

studio_price = (studio_price * number_nights) * studio_discount
apartment_price = (apartment_price * number_nights) * apartment_discount

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")