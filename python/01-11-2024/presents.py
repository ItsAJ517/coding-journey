# Presents

# This program gives a user £200 to spend on presents.
# They will keep entering the price of each present until they reach exactly £200.

# How to run: this file does not need any additional libraries and can be run directly in the command line
print("Presents")

print("\nYou have £200 to spend on presents.")
print("I will ask you to input the price of each present, until the total exceeds £200.")
print("You can have as many presents as you want, as long as you don't exceed £200.")

total = 0

while total <= 200:
    price = float(input("\nEnter the price of your present: £"))
    
    if total + price <= 200:
        total += price
        
        if total == 200:
            break
        print(f"Total so far: £{total}")
        
    elif total + price > 200:
        print(f"Limit exceeded. You cannot include that £{price} present.")

print("You have spent £200!")
input("Press enter to close the program.")
