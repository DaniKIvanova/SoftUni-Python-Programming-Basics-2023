number_of_joinery = int(input())
type_of_joinery = input()
shipment_method = input()
deliver = 0
joinery_price_off = 0

delivery_fee = 60
joinery_size_ninety = 110
joinery_size_onehundred = 140
joinery_size_onehundred_thurty = 190
joinery_size_twohundred = 250

if number_of_joinery < 10:
    print("Invalid order")
    stop_under_order = False

else:
    if "90X130" == type_of_joinery:
        if number_of_joinery <= 30:
            joinery_price_off = number_of_joinery * joinery_size_ninety

        if number_of_joinery > 30:
            joinery_price_off = number_of_joinery * joinery_size_ninety
            joinery_price_off = joinery_price_off - joinery_price_off * 0.05

        if number_of_joinery > 60:
            joinery_price_off = number_of_joinery * joinery_size_ninety
            joinery_price_off = joinery_price_off - joinery_price_off * 0.08

    elif "100X150" == shipment_method:
        if number_of_joinery <= 40:
            joinery_price_off = number_of_joinery * joinery_size_onehundred

        if number_of_joinery > 40:
            joinery_price_off = number_of_joinery * joinery_size_onehundred
            joinery_price_off = joinery_price_off - joinery_price_off * 0.06

        if number_of_joinery > 80:
            joinery_price_off = number_of_joinery * joinery_size_onehundred
            joinery_price_off = joinery_price_off - joinery_price_off * 0.10

    elif "130X180" == shipment_method:
        if number_of_joinery <= 20:
            joinery_price_off = number_of_joinery * joinery_size_onehundred_thurty

        if number_of_joinery > 20:
            joinery_price_off = number_of_joinery * joinery_size_onehundred_thurty
            joinery_price_off = joinery_price_off - joinery_price_off * 0.07

        if number_of_joinery > 50:
            joinery_price_off = number_of_joinery * joinery_size_onehundred_thurty
            joinery_price_off = joinery_price_off - joinery_price_off * 0.12

    elif "200X300" == shipment_method:
        if number_of_joinery <= 25:
            joinery_price_off = number_of_joinery * joinery_size_twohundred

        if number_of_joinery > 25:
            joinery_price_off = number_of_joinery * joinery_size_twohundred
            joinery_price_off = joinery_price_off - joinery_price_off * 0.09

        if number_of_joinery > 50:
            joinery_price_off = number_of_joinery * joinery_size_twohundred
            joinery_price_off = joinery_price_off - joinery_price_off * 0.14

    if "With delivery" == deliver:
        joinery_price_off = joinery_price_off + delivery_fee

    if "Without delivery" == deliver:
        joinery_price_off = joinery_price_off

    if number_of_joinery > 99:
        joinery_price_off = joinery_price_off - joinery_price_off * 0.04

    print(f"{joinery_price_off:.2f} BGN")