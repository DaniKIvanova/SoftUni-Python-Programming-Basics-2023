sum_prime = 0
sum_non_prime = 0

while True:
    number = input()

    if number == "stop":
        break

    current_number = int(number)
    is_prime = True

    if current_number < 0:
        print("Number is negative.")
        continue

    for num in range(2, current_number):
        if current_number % num == 0:
            is_prime = False
            break

    if is_prime:
        sum_prime += current_number
    else:
        sum_non_prime += current_number

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")