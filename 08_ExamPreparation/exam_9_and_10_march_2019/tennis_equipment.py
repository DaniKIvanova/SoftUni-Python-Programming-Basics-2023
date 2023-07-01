import math

price_of_one_tennis_racket = float(input())
number_of_tennis_racket = int(input())
number_of_pair_sneakers = int(input())

price_of_tennis_racket = number_of_tennis_racket * price_of_one_tennis_racket
price_of_pair_sneakers = price_of_one_tennis_racket / 6
price_of_all_sneakers = number_of_pair_sneakers * price_of_pair_sneakers
price_of_remaining_equipment = (price_of_tennis_racket + price_of_all_sneakers) * 0.20
total_price = price_of_tennis_racket + price_of_all_sneakers + price_of_remaining_equipment
price_of_djokovic = total_price / 8
price_of_sponsors = total_price * 7 / 8

print(f"Price to be paid by Djokovic {math.floor(price_of_djokovic)}")
print(f"Price to be paid by sponsors {math.ceil(price_of_sponsors)}")