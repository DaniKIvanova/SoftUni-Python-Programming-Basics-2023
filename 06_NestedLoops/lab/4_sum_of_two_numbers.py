number = int(input())
number_end = int(input())
magic_number = int(input())

combinations = 0
stop = False

for num1 in range(number, number_end + 1):
    for num2 in range(number, number_end + 1):
        combinations += 1
        if num1 + num2 == magic_number:
            stop += True
            print(f"Combination N:{combinations} ({num1} + {num2} = {magic_number})")
            break
    if stop:
        break
if not stop:
    print(f"{combinations} combinations - neither equals {magic_number}")