# Password generator

# This program takes 4 user inputs:
#  1. pet name
#  2. favourite holiday destination
#  3. house number
#  4. birth year

# These variables are used to make a password for the user.

# How to run: this file does not need any additional libraries and can be run directly in the command line.
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
password = str(prefix) + holiday + pet_name + str(suffix)

print("Here is your password: ")
print(password)
input("Press <Enter> to close the program!")
