egg_size = input()
egg_color = input()
batches = int(input())

price_batches = 0
if egg_size == "Large":
    if egg_color == "Red":
        price_batches += 16
    elif egg_color == "Green":
        price_batches += 12
    elif egg_color == "Yellow":
        price_batches += 9
elif egg_size == "Medium":
    if egg_color == "Red":
        price_batches += 13
    elif egg_color == "Green":
        price_batches += 9
    elif egg_color == "Yellow":
        price_batches += 7
elif egg_size == "Small":
    if egg_color == "Red":
        price_batches += 9
    elif egg_color == "Green":
        price_batches += 8
    elif egg_color == "Yellow":
        price_batches += 5

price = batches * price_batches
expenses = price * 0.35
total_sum = price - expenses

print(f"{total_sum:.2f} leva.")