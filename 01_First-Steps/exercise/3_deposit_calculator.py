amount_deposited = float(input())
term_of_the_deposit_months = float(input())
year_interest_rate = float(input())

total_sum = amount_deposited + term_of_the_deposit_months * ((amount_deposited * year_interest_rate) / 12)

print(total_sum)