name_of_airline = input()
adults_tickets = int(input())
kids_tickets = int(input())
net_price_adult = float(input())
price_service_fee = float(input())

net_price_kid = net_price_adult - net_price_adult * 0.70
total_price_adult = net_price_adult + price_service_fee
total_price_kid = net_price_kid + price_service_fee
total_price = (kids_tickets * total_price_kid) + (adults_tickets * total_price_adult)
profit = total_price * 0.20
print(f"The profit of your agency from {name_of_airline} tickets is {profit:.2f} lv.")