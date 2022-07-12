tickets = int(input('Enter the number of required tickets: '))
price = 0
for i in range(1, tickets + 1):
    age = int(input(f"Enter the age of visitor for ticket {i}: "))
    if age < 18:
        price += 0
    elif 18 <= age <= 25:
        price += 990
    else:
        price += 1390
if tickets > 3:
    price *= 0.9
print(f"Amount payable {price}")
