locations = int(input())

for _ in range(1, locations + 1):
    expected_average_yield = float(input())
    days = int(input())
    average_yield = 0

    for _ in range(1, days + 1):
        current_yield = float(input())
        average_yield += current_yield

    average_per_location = average_yield / days
    diff = abs(average_per_location - expected_average_yield)

    if average_per_location < expected_average_yield:
        print(f"You need {diff:.2f} gold.")
    else:
        print(f"Good job! Average gold per day: {average_per_location:.2f}.")