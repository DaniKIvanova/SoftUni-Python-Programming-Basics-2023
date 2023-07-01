number_tournaments = int(input())
starting_points = int(input())

tournaments_points = 0
wins = 0

for tournament in range(number_tournaments):
    tournament_output = input()

    if tournament_output == "W":
        tournaments_points += 2000
        wins += 1

    elif tournament_output == "F":
        tournaments_points += 1200

    elif tournament_output == "SF":
        tournaments_points += 720

print(f"Final points: {starting_points + tournaments_points}")
print(f"Average points: {int(tournaments_points / number_tournaments)}")
print(f"{(wins / number_tournaments) * 100:.2f}%")