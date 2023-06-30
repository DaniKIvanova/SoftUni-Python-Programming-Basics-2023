year_fee = int(input())

shoes = year_fee - year_fee * 0.40
clothes = shoes - shoes * 0.20
ball = clothes / 4
accessories = ball / 5

total_price = year_fee + shoes + clothes + ball + accessories

print(total_price)