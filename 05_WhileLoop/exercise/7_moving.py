width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height
filled_space = 0

while free_space > filled_space:
    number_of_cartons = input()
    if number_of_cartons == "Done":
        print(f"{free_space - filled_space} Cubic meters left.")
        break
    filled_space += int(number_of_cartons)
else:
    print(f"No more free space! You need {filled_space - free_space} Cubic meters more.")