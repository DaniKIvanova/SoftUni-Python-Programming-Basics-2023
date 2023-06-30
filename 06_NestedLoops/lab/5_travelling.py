saved_money = 0

while True:
    destination = input()
    if destination == "End":
        break
    need_money = float(input())
    saved_money = 0
    while saved_money < need_money:
        money = float(input())
        saved_money += money
    print(f"Going to {destination}!")