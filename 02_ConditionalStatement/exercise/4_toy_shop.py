excursion_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

PUZZLE_PRICE = 2.60
TALKING_DOLL_PRICE = 3
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

amount_of_toys = (puzzles * PUZZLE_PRICE) + \
                 (talking_dolls * TALKING_DOLL_PRICE) + \
                 (teddy_bears * TEDDY_BEAR_PRICE) + \
                 (minions * MINION_PRICE) + \
                 (trucks * TRUCK_PRICE)
number_of_toys = puzzles + talking_dolls + teddy_bears + minions + trucks

if number_of_toys >= 50:
    amount_of_toys *= 0.75

amount_of_toys *= 0.90

if amount_of_toys >= excursion_price:
    print(f"Yes! {amount_of_toys - excursion_price:.2f} lv left.")
else:
    print(f"Not enough money! {excursion_price - amount_of_toys:.2f} lv needed.")