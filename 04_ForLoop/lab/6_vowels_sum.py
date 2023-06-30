text = input()

letters = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}

sum_letters = 0
letter_check = ("a", "e", "i", "o", "u")

for letter in text:
    if letter in letter_check:
        sum_letters += letters[letter]

print(sum_letters)