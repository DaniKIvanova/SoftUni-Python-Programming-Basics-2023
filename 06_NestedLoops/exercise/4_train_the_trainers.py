number_of_judges = int(input())

average_score = 0
average_success = 0

while True:
    presentation_name = input()

    if presentation_name == "Finish":
        break

    number_of_grades = 0

    for _ in range(number_of_judges):
        number_of_grades += float(input())

    average_success += number_of_grades
    average_score += number_of_judges

    print(f"{presentation_name} - {number_of_grades / number_of_judges:.2f}.")

print(f"Student's final assessment is {average_success / average_score:.2f}.")