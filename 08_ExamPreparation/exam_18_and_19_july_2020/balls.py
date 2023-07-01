import math
number_of_balls = int(input())

while True:
    ball = "red" or "orange" or "yellow" or "white" or "black"
    red_balls = 0
    orange_balls = 0
    yellow_balls = 0
    white_balls = 0
    black_balls = 0
    points = 0
    balls_out_color = 0
    for ball in range(0, number_of_balls):
        if ball == "red":
            points += 5
            red_balls += 1
        elif ball == "orange":
            points += 10
            orange_balls += 1
        elif ball == "yellow":
            points += 15
            yellow_balls += 1
        elif ball == "white":
            points += 20
            white_balls += 1
        elif ball == "black":
            points = math.floor(points / 2)
            black_balls += 1
        elif ball != "red" or "orange" or "yellow" or "white" or "black":
            balls_out_color += 1

    print(f"Total points: {points}")
    print(f"Red balls: {red_balls}")
    print(f"Orange balls: {orange_balls}")
    print(f"Yellow balls: {yellow_balls}")
    print(f"White balls: {white_balls}")
    print(f"Other colors picked: {balls_out_color}")
    print(f"Divides from black balls: {black_balls}")