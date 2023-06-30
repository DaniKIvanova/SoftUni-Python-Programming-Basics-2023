required_amount_of_nylon = int(input())
required_amount_of_paint_liters = int(input())
amount_of_thinner_liters = int(input())
hours_job_done = int(input())

NYLON = 1.50
PAINT = 14.50
THINNER = 5
amount_for_bags = 0.40

required_amount_of_nylon += 2
required_amount_of_paint_liters += required_amount_of_paint_liters * 0.10

total_amount_for_materials = (required_amount_of_nylon * NYLON) + \
                             (required_amount_of_paint_liters * PAINT) + \
                             (amount_of_thinner_liters * THINNER) + \
                             amount_for_bags
wages_to_the_masters = total_amount_for_materials * 0.30
final_amount = total_amount_for_materials + (wages_to_the_masters * hours_job_done)

print(final_amount)