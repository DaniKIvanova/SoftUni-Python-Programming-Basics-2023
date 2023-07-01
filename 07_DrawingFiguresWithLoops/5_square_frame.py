n = int(input())

for row in range(1, n + 1):
    if row == 1 or n == row:
        print("+ " + (n - 2) * "- " + "+ ")
    else:
        print("| " + (n -2) * "- " + "| ")