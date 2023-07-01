price_of_flour_per_kilogram = float(input())
kilograms_of_flour = float(input())
kilograms_of_sugar = float(input())
number_of_eggshells = int(input())
packets_of_yeast = int(input())

price_kilograms_of_sugar = price_of_flour_per_kilogram * 0.75
price_one_eggshells = price_of_flour_per_kilogram * 1.1
price_one_packets_of_yeast = price_kilograms_of_sugar * 0.2
sum_of_flour = price_of_flour_per_kilogram * kilograms_of_flour
sum_of_sugar = price_kilograms_of_sugar * kilograms_of_sugar
sum_of_eggs = price_one_eggshells * number_of_eggshells
sum_of_yeast = price_one_packets_of_yeast * packets_of_yeast
total_sum = sum_of_flour + sum_of_sugar + sum_of_eggs + sum_of_yeast

print(f"{total_sum:.2f}")