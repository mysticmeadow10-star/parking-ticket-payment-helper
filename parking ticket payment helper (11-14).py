def get_change(paid, price):
    return paid - price

print("Welcome to the Parking Ticket Machine! Ticket costs 50 cents.")
total = 0

while True:
    coin = int(input("Insert coin (5, 10, 25): "))
    
    
    if coin != 5 and coin != 10 and coin != 25:
        print("Invalid coin! Try again.")
        continue
        
    total += coin
    print("Total inserted so far:", total)
    
    
    if total >= 50:
        break

change = get_change(total, 50)


if change == 0:
    pass
else:
    print("Your change is:", change)

print("Thank you for paying! Here is your parking ticket.")