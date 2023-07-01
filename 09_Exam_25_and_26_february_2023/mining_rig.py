import math

price_of_one_video_card = int(input())
price_of_one_transition = int(input())
price_of_current_consumed = float(input())
profit_one_card_per_day = float(input())

video_cards = 13
transition = 13
second_hand_components = 1000

total_price_video_cards = price_of_one_video_card * video_cards
total_price_transitions = price_of_one_transition * transition
total_price = total_price_video_cards + total_price_transitions + second_hand_components
price_of_card_per_day = profit_one_card_per_day - price_of_current_consumed
total_price_per_day_card = video_cards * price_of_card_per_day
return_days = total_price / total_price_per_day_card

print(total_price)
print(math.ceil(return_days))