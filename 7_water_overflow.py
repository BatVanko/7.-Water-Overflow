capacity_liters = 255
number_of_comands = int(input())
filled_amount = 0
for _ in range (number_of_comands):
    income_litres = int(input())
    if income_litres + filled_amount > capacity_liters:
            print("Insufficient capacity!")
            continue
    else:
        filled_amount += income_litres

print(filled_amount)

