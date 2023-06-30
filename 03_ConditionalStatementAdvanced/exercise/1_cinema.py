type_screening = input()
rows = int(input())
columns = int(input())

ticket_revenue = 0
hall_capacity = rows * columns

if type_screening == "Premiere":
    ticket_revenue = hall_capacity * 12.00
elif type_screening == "Normal":
    ticket_revenue = hall_capacity * 7.50
elif type_screening == "Discount":
    ticket_revenue = hall_capacity * 5.00

print(f"{ticket_revenue:.2f} leva")

