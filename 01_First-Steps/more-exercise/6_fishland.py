price_of_mackerel_kilo = float(input())
price_of_sprinkle_kilo = float(input())
bonito_kilo = float(input())
horse_mackerel_kilo = float(input())
mussels_kilo = float(input())

PRICE_MUSSELS_KILO = 7.50

total_mussels = mussels_kilo * PRICE_MUSSELS_KILO
price_bonito_kilo = (((price_of_mackerel_kilo * 0.60) + price_of_mackerel_kilo) * bonito_kilo)
price_horse_mackerel_kilo = (((price_of_sprinkle_kilo * 0.80) + price_of_sprinkle_kilo) * horse_mackerel_kilo)
total_bill = total_mussels + price_bonito_kilo + price_horse_mackerel_kilo

print(f"{total_bill:.2f}")