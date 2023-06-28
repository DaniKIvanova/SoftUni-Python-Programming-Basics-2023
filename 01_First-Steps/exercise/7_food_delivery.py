number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegetarian_menus = int(input())

chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
cost_to_delivery = 2.50

total_price_of_the_menus = (number_of_chicken_menus * chicken_menu) + \
                           (number_of_fish_menus * fish_menu) + \
                           (vegetarian_menu * vegetarian_menu)
dessert_price = total_price_of_the_menus * 0.20
total_price_of_the_order = total_price_of_the_menus + dessert_price + cost_to_delivery

print(total_price_of_the_order)