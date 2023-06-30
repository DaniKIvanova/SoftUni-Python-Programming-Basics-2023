range_numbers = int(input())
left_sum = 0
right_sum = 0

for num in range(range_numbers * 2):
    current_num = int(input())
    if num < range_numbers:
        left_sum += current_num
    elif num >= range_numbers:
        right_sum += current_num

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")