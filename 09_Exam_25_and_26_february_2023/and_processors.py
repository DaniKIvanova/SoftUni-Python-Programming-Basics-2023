import math

number_of_processors = int(input())
number_of_employees = int(input())
working_days = int(input())

hour_total = number_of_employees * working_days * 8
made = math.floor(hour_total / 3)

if made < number_of_processors:
    processors = number_of_processors - made
    lost = processors * 110.10
    print(f"Losses: -> {lost:.2f} BGN")
elif made >= number_of_processors:
    processors_more = made - number_of_processors
    profit = processors_more * 110.10
    print(f"Profit: -> {profit:.2f} BGN")