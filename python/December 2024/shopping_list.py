# Shopping list

# The user can add and remove items from a shopping list.
# They can also view the contents of their shopping list.

# How to run: this program does not require any additional libraries and can be run directly in the command line.

shopping_items = []

print("Shoppping List Program\n")

# Main program begins here
while True:
    option = input("""\nEnter (1) Add item
      (2) Delete item
      (3) View items
      (0) Exit
Option: """)
    
    #[1] Add item
    if option == "1":
        item = input("Enter the item you would like to add: ")
        
        # Selection statements used to avoid errors
        if item in shopping_items:
            print(f"'{item}' is already in your shopping list")
        else:
            shopping_items.append(item)
            print("Item added succesfully")

    #[2] Remove item
    elif option == "2":
        item = input("Enter the item you would like to remove: ")

        # Selection statements used to avoid errors
        if item in shopping_items:
            shopping_items.remove(item)
            print("Item removed succesfully")
        else:
            print("Item not in list")

    #[3] View items
    elif option == "3":
        print(shopping_items)
    
    #[0] Exit
    elif option == "0":
        break
    
    #[X] Invalid inputs
    else:
        print("Invalid choice")


input("Press <Enter> to close the program")
