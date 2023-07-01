toy_price = 5
sweater_price = 15
kids = 0
adults = 0
toys = 0
sweaters = 0

while True:
    line = input()
    if line == "Christmas":
        break
    else:
        number = int(line)
        if number <= 16:
            toys += 1
            kids += 1
        else:
            adults += 1
            sweaters += 1

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {toys * toy_price}")
print(f"Money for sweaters: {sweaters * sweater_price}")