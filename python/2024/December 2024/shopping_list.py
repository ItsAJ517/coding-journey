# Shopping list

# The user can add and remove items from a shopping list.
# They can also view the contents of their shopping list.
# This program handles any invalid user inputs as well.

# How to run: this file does not require any additional libraries and can be run directly in the command line.

shopping_items = []

# Welcome message
print("Shoppping List Program\n")

# Main program begins here
while True:
    # User enters option
    option = input("""\nEnter (1) Add item
      (2) Delete item
      (3) View items
      (0) Exit
Option: """)
    
    #[1] Add item
    if option == "1":
        # User enter item
        item = input("Enter the item you would like to add: ")
        
        # Check if item is in the shopping list to avoid duplicate items
        if item in shopping_items:
            print(f"'{item}' is already in your shopping list")
        else:
            shopping_items.append(item) # add item
            print("Item added succesfully")

    #[2] Remove item
    elif option == "2":
        # User enters item
        item = input("Enter the item you would like to remove: ")

        # Check if item is in the shopping list to avoid errors
        if item in shopping_items:
            shopping_items.remove(item) # remove item
            print("Item removed succesfully")
        else:
            print("Item not in list")

    #[3] View items
    elif option == "3":
        print(shopping_items)
    
    #[0] Exit
    elif option == "0":
        break # end loop
    
    #[X] Invalid inputs
    else:
        # Tell user to enter correct option
        print("Invalid choice")


input("Press <Enter> to close the program")

# Insights: I was using a loop control variable for my 'while' loop before. However, my teacher pointed out that using an endless loop is easier.
# My program was also much longer before as I had the 'option' input variable inside each selection statement rather than at the top of the loop
# Improvements: when viewing the shopping list, I could have formatted it in a nicer way.
