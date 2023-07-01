number_of_guests = int(input())
price_envelope_for_one_person = float(input())
budget = float(input())

reservation = 0

if number_of_guests < 10:
    reservation = price_envelope_for_one_person
elif 10 <= number_of_guests <= 15:
    reservation = price_envelope_for_one_person - (price_envelope_for_one_person * 0.15)
elif 15 < number_of_guests <= 20:
    reservation = price_envelope_for_one_person - (price_envelope_for_one_person * 0.20)
elif number_of_guests > 20:
    reservation = price_envelope_for_one_person - (price_envelope_for_one_person * 0.25)

cake_price = budget - (budget * 0.90)

total_sum = (number_of_guests * reservation) + cake_price

if total_sum > budget:
    print(f"No party! {total_sum - budget:.2f} leva needed.")
elif total_sum < budget:
    print(f"It is party time! {budget - total_sum:.2f} leva left.")