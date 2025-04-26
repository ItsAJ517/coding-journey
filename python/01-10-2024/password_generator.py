import random

print("Password Generator")
# User inputs
pet_name = input("\nEnter your pet's name: ").upper()
holiday = input("Enter your favourite holiday destination: ").upper()
house_num = input("Enter your house number: ")
birth_year = input("Enter your birth year: ")

# Variables
prefix = random.randint(0, int(house_num) + int(birth_year))
suffix = int(house_num) + int(birth_year)
password = str(prefix) + holiday.upper() + pet_name.upper() + str(suffix)

print("Here is your password: ")
input(password)
