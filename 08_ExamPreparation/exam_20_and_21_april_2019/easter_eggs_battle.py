number_of_eggs_first_player = int(input())
number_of_eggs_second_player = int(input())

player_one_eggs_left = number_of_eggs_first_player
player_two_eggs_left = number_of_eggs_second_player

while True:
    winner = input()

    if winner == "End":
        print(f"Player one has {player_one_eggs_left} eggs left.")
        print(f"Player two has {player_two_eggs_left} eggs left.")
        break

    if winner == "one":
        player_two_eggs_left -= 1
    else:
        player_one_eggs_left -= 1

    if player_one_eggs_left == 0:
        print(f"Player one is out of eggs. Player two has {player_two_eggs_left} eggs left.")
        break
    elif player_two_eggs_left == 0:
        print(f"Player two is out of eggs. Player one has {player_one_eggs_left} eggs left.")
        break
