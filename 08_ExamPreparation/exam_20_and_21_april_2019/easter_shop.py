starting_amount_of_eggs = int(input())
total_eggs_sold = 0
total_eggs = starting_amount_of_eggs

while True:
    command = input()

    if command == "Close":
        print("Store is closed!")
        print(f"{total_eggs_sold} eggs sold.")
        break

    else:
        number_eggs = int(input())

    if command == "Buy":
        total_eggs -= number_eggs
        total_eggs_sold += number_eggs
    elif command == "Fill":
        total_eggs += number_eggs

    if total_eggs < 0:
        print("Not enough eggs in store!")
        print(f"You can buy only {total_eggs + number_eggs}.")
        break