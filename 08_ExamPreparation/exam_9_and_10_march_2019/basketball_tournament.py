tournament_name = input()

wins = 0
loses = 0

while tournament_name != "End of tournaments":
    number_of_games = int(input())

    for game in range(1, number_of_games + 1):
        home_team = int(input())
        away_team = int(input())
        difference = abs(home_team - away_team)

        if home_team > away_team:
            wins += 1
            result = "win"
            print(f"Game {game} of tournament {tournament_name}: win with {difference} points.")
        elif home_team < away_team:
            loses += 1
            result = "lost"
            print(f"Game {game} of tournament {tournament_name}: lost with {difference} points.")

    tournament_name = input()

print(f"{(wins / (wins + loses)) * 100:.2f}% matches win")
print(f"{(loses / (wins + loses)) * 100:.2f}% matches lost")
