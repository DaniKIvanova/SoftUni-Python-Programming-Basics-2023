width = int(input())
length = int(input())

number_of_pieces = width * length
pieces_taken = 0

while number_of_pieces >= pieces_taken:
    pieces = input()
    if pieces == "STOP":
        print(f"{number_of_pieces - pieces_taken} pieces are left.")
        break
    pieces_taken += int(pieces)
else:
    print(f"No more cake left! You need {pieces_taken - number_of_pieces} pieces more.")