number_floors = int(input())
number_rooms = int(input())

for floors in range(number_floors, 0, -1):
    for rooms in range(number_rooms):
        if floors == number_floors:
            print(f"L{floors}{rooms}", end=" ")
        else:
            if floors % 2 != 0:
                print(f"A{floors}{rooms}", end=" ")
            else:
                print(f"O{floors}{rooms}", end=" ")
    print(" ")