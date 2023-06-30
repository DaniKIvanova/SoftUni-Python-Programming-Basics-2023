price_kilo_vegetable = float(input())
price_kilo_fruits = float(input())
total_kilograms_vegetables = int(input())
total_kilograms_fruits = int(input())

euro = 1.94

income_all_fruits_and_vegetables = total_kilograms_vegetables * price_kilo_vegetable + \
                                   total_kilograms_fruits * price_kilo_fruits
income_all_fruits_and_vegetables_euro = income_all_fruits_and_vegetables / euro

print(f"{income_all_fruits_and_vegetables_euro:.2f}")