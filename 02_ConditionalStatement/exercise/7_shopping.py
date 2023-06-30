budget = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_ram_memory = int(input())

VIDEO_CARD = 250
PROCESSOR = number_video_cards
RAM_MEMORY = number_video_cards

sum_video_cards = number_video_cards * VIDEO_CARD
sum_processors = (number_processors * sum_video_cards) * 0.35
sum_ram_memory = (number_ram_memory * sum_video_cards) * 0.10

total_sum = sum_video_cards + sum_processors + sum_ram_memory

if number_video_cards > number_processors:
    total_sum *= (1 - 0.15)

if budget >= total_sum:
    print(f"You have {budget - total_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_sum - budget:.2f} leva more!")