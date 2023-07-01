number_easter_bread = int(input())
number_of_shelled_eggs = int(input())
kilograms_of_cookies = int(input())

easter_bread = 3.20
eggs = 4.35
cookies = 5.40
paint_for_eggs = 0.15

price_easter_breads = number_easter_bread * easter_bread
price_eggs = number_of_shelled_eggs * eggs
price_cookies = kilograms_of_cookies * cookies
price_paint_for_eggs = (number_of_shelled_eggs * 12) * paint_for_eggs
total_price = price_easter_breads + price_eggs + price_cookies + price_paint_for_eggs

print(f"{total_price:.2f}")