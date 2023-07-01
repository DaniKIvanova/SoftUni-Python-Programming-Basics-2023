month = input()
number_of_hours = int(input())
number_of_people = int(input())
time_of_day = input()
price_of_hour = 0

if month == "march" or month == "april" or month == "may":
    if time_of_day == "day":
        price_of_hour = 10.50
    elif time_of_day == "night":
        price_of_hour = 8.40
elif month == "june" or month == "july" or month == "august":
    if time_of_day == "day":
        price_of_hour = 12.60
    elif time_of_day == "night":
        price_of_hour = 10.20

if number_of_people >= 4:
    price_of_hour *= 0.90

if number_of_hours >= 5:
    price_of_hour *= 0.50

total_price = (price_of_hour * number_of_people) * number_of_hours

print(f"Price per person for one hour: {price_of_hour:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")
