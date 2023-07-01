player_name = input()

field = input()
player_starting_points = 301
successful_shot = 0
unsuccessful_shot = 0

while field != "Retire":
    points = int(input())

    if "Double" == field:
        points *= 2

    elif "Triple" == field:
        points *= 3

    if points <= player_starting_points:
        successful_shot += 1
        player_starting_points -= points

        if not player_starting_points:
            print(f"{player_name} won the leg with {successful_shot} shots.")
            break

    else:
        unsuccessful_shot += 1

    field = input()

else:
    print(f"{player_name} retired after {unsuccessful_shot} unsuccessful shots.")
