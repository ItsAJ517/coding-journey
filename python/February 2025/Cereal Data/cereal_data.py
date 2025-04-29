# Extracting cereal data

# This program extracts data from the CSV file named 'cereals.csv' as a list
# It then presents different statistics in the data

# How to run: for this file, you will also need to download 'cereals.csv'. Make sure that this file and the CSV file are both in the same directory.
# After that, you can run the program as normal in the command line.

import csv

# Extract data
with open('cereals.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    data = list(csv_reader)

print("Cereal Data")
print()

# Display number of Kelloggs and other brand cereals
kelloggs_cereals = 0
other_cereals = 0

# Find data
for i in range(1, len(data)):
    if data[i][1].lower() == "kelloggs":
        kelloggs_cereals += 1
    else:
        other_cereals += 1

# Print details
print(f"There are {kelloggs_cereals} Kelloggs cereals in the data.")
print(f"There are {other_cereals} other cereals.")
input()

#Calories
less_than_100kcal = 0
over_100kcal = 0

for i in range(1, len(data)):
    if float(data[i][3]) < 100:
        less_than_100kcal += 1
    else:
        over_100kcal += 1


print(f"{less_than_100kcal} cereals have less than 100 calories.")
print(f"{over_100kcal} cereals have over 100 calories.")
input()

#Sodium
less_than_200_sodium = 0
over_200_sodium = 0

for i in range(1, len(data)):     
    if float(data[i][6]) < 200:
        less_than_200_sodium += 1
    else:
        over_200_sodium += 1


print(f"{less_than_200_sodium} cereals have less than 200 sodium.")
print(f"{over_200_sodium} cereals have over 200 sodium.")
input()

#Carbohydrates
less_than_15_carbs = 0
over_15_carbs = 0

for i in range(1, len(data)):
    if float(data[i][8]) < 15:
        less_than_15_carbs += 1
    else:
        over_15_carbs += 1


print(f"{less_than_15_carbs} cereals have less than 15 carbs.")
print(f"{over_15_carbs} cereals have over 15 carbs.")
input()

#Ratings
rating_under_50 = 0
rating_above_50 = 0

cereal_with_highest_rating = [0]
cereal_with_lowest_rating = [999]

for i in range(len(data)):
    if float(data[i][-1]) <= 50:
        rating_under_50 += 1
    else:
        rating_above_50 += 1

    if float(data[i][-1]) > float(cereal_with_highest_rating[-1]):
        cereal_with_highest_rating = data[i]
    if float(data[i][-1]) < float(cereal_with_lowest_rating[-1]):
        cereal_with_lowest_rating = data[i]
        

print(f"{rating_under_50} cereals have a rating under 50.")
print(f"{rating_above_50} cereals have a rating above 50.")
print()

print(f"The cereal with the highest rating was {cereal_with_highest_rating[0]}, made by {cereal_with_highest_rating[1]}, " \
      f"with a rating of {cereal_with_highest_rating[-1]}.")

print(f"The cereal with the lowest rating was {cereal_with_lowest_rating[0]}, made by {cereal_with_lowest_rating[1]}, " \
      f"with a rating of {cereal_with_lowest_rating[-1]}.")

input("Press enter to close the program!")
