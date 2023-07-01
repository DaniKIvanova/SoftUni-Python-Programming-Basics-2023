luggage_cost = float(input())
kg_of_baggage = float(input())
days_until_travel = int(input())
number_of_luggage = int(input())

baggage_fee = 0
days_fee = 0

if kg_of_baggage < 10:
    baggage_fee = luggage_cost * 0.20
elif 10 <= kg_of_baggage <= 20:
    baggage_fee = luggage_cost * 0.50
else:
    baggage_fee = luggage_cost

if days_until_travel > 30:
    days_fee = baggage_fee * 0.10
elif 7 <= days_until_travel <= 30:
    days_fee = baggage_fee * 0.15
else:
    days_fee = baggage_fee * 0.40

total_price = (baggage_fee + days_fee) * number_of_luggage

print(f"The total price of bags is: {total_price:.2f} lv.")