number = int(input())

current = 0
is_the_end = False

for row in range(1, number + 1):
    for num in range(1, row + 1):
        current += 1

        print(current, end=" ") if row != num else print(current)

        if current == number:
            is_the_end = True
            break
    if is_the_end:
        break