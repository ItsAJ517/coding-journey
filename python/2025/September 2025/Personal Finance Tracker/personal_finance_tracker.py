# Personal Finance Tracker

# This program allows a user to keep track of their finances.
# It includes several functions such as adding transactions, viewing remaining balance, and editing budgets.

# How to run: for this file, please make sure to download this program as well as the JSON file, 'user_data.json'.
# When running the program, make sure both files are in the exact same directory.

# Modules
import json
from datetime import *
import calendar


### FUNCTIONS ###

def chooseOption(options_list, option_name):
    print(f"\n{option_name}:")

    for i in range(len(options_list)):
        print(f"{i+1}. {options_list[i]}")
    
    while True:
        try:
            index = int(input("Select one: "))

            if 1 <= index <= len(options_list):
                option = options_list[index-1]
                break
                
            print("Invalid choice")
        
        except ValueError:
            print("Invalid choice")
    
    return option

def calcDate(str_date):
    yr = int(str_date[:4])
    mnth = int(str_date[5:7])
    dy = int(str_date[8:])

    return_date = date(yr, mnth, dy)
    return return_date
    

def addMonth(transact_dt):
    yr = transact_dt.year
    mnth = transact_dt.month + 1

    if mnth > 12:
        mnth = 1
        yr += 1

    try:
        transact_dt = transact_dt.replace(yr, mnth)
    
    except ValueError:
        _, num_days = calendar.monthrange(yr, mnth)
        transact_dt = transact_dt.replace(yr, mnth, num_days)

    return transact_dt

def getTimePeriodRange(time_perd, end_date=None):
    today = date.today()

    if time_perd == "this week":
        start = today - timedelta(days=today.weekday())
        end = start + timedelta(days=6)

    elif time_perd == "this month":
        start = today.replace(day=1)
        
        if today.month == 12:
            first_of_next_month = today.replace(today.year + 1, 1, 1)
        else:
            first_of_next_month = today.replace(month=today.month+1, day=1)
        
        end = first_of_next_month - timedelta(days=1)
    
    elif time_perd == "next three months":
        start = end_date
        end = start

        for i in range(3):
            end = addMonth(end)

    else:
        start = today.replace(month=1, day=1)
        end = today.replace(month=12, day=31)
    
    return start, end


def balanceBeforeStart(start, transactions):
    # Calculate total income and expenses before the start of the time period
    total_income = 0
    total_expense = 0

    for t in transactions:
        # Transaction date
        transaction_date = calcDate(t["date"])
        
        # Check if transaction date is before the start of the time period
        if transaction_date < start:
            transaction_money = recurringTransactions(t, start, transaction_date)

            if t["type"] == "expense":
                total_expense += transaction_money
            else:
                total_income += transaction_money
    
    # Calculate balance
    balance = total_income - total_expense
    return balance


def balanceWithin(start, end, transactions):
    total_income_time_period = 0
    total_expense_time_period = 0

    # This list will store the details for each transaction
    transaction_names_list = []

    for t in transactions:
        transaction_date = calcDate(t["date"])
        transaction_amount, details = recurringTransactionsWithin(t, start, end, transaction_date)

        if transaction_amount > 0:
            if t["type"] == "expense":
                total_expense_time_period += transaction_amount
                details = "-" + details
            else:
                total_income_time_period += transaction_amount
                details = "+" + details
        
            transaction_names_list.append(details)


    return total_income_time_period, total_expense_time_period, transaction_names_list



def recurringTransactions(transact, start_time_period, transact_date):
    transact_money = 0
    freq = transact["frequency"]
    amount = transact["amount"]

    # One-time transactions
    if freq == "one-time":
        transact_money += amount

    # Weekly transactions
    elif freq == "weekly":
        while transact_date < start_time_period:
            transact_money += amount
            transact_date += timedelta(weeks=1)
    
    # Monthly transactions
    elif freq == "monthly":
        while transact_date < start_time_period:
            transact_money += amount
            transact_date = addMonth(transact_date)
    
    # Yearly transactions
    else:
        while transact_date < start_time_period:
            transact_money += amount
            transact_date = transact_date.replace(year=transact_date.year + 1)
    
    return transact_money


def recurringTransactionsWithin(transact, start_time_period, end_time_period, transact_date):
    transact_money = 0
    freq = transact["frequency"]
    amount = transact["amount"]

    # One-time transactions
    if freq == "one-time":
        # Check if the transaction is within the time period
        if start_time_period <= transact_date <= end_time_period:
            transact_money += amount


    # Weekly transactions
    elif freq == "weekly":
        # Move the transaction date within the time period
        while transact_date < start_time_period:
            transact_date += timedelta(weeks=1)

        
        # Add the transaction amount until the end of the time period is reached
        while transact_date <= end_time_period:
            transact_money += amount
            transact_date += timedelta(weeks=1)


    # Monthly transactions
    elif freq == "monthly":
        # Move the transaction date within the time period
        while transact_date < start_time_period:
            transact_date = addMonth(transact_date)

        
        # Add the transaction amount until the end of the time period is reached
        while transact_date <= end_time_period:
            transact_money += amount
            transact_date = addMonth(transact_date)


    # Yearly transactions
    else:
        # Move the transaction date within the time period
        while transact_date < start_time_period:
            transact_date = transact_date.replace(year=transact_date.year + 1)

        
        # Add the transaction amount until the end of the time period is reached
        while transact_date <= end_time_period:
            transact_money += amount
            transact_date = transact_date.replace(year=transact_date.year + 1)
    

    transact_name = f" £{transact_money}: {transact["transact_name"]}, {transact["category"]} {transact["date"], freq}"

    return transact_money, transact_name


def printAllTransactions(transacts):
    for t in transacts:
        printTransactDetails(t)


def printTransactDetails(transact):
    print("\n###############")
    print(f"Name: {transact["transact_name"]}")
    print(f"Date: {transact["date"]}")
    print(f"Amount: £{transact["amount"]}")
    print(f"Category: {transact["category"]}")
    print(f"Type: {transact["type"]}")
    print(f"Frequency: {transact["frequency"]}")
    print("###############")


def calcCategorySpending(transactions, transact_category):
    start_month, end_month = getTimePeriodRange("this month")
    total_category_spending = 0

    for t in transactions:
        if t["category"] == transact_category:
            transaction_date = calcDate(t["date"])

            transaction_amount, _ = recurringTransactionsWithin(t, start_month, end_month, transaction_date)

            if t["type"] == "expense":
                total_category_spending += transaction_amount
            else:
                total_category_spending -= transaction_amount
    
    return total_category_spending

### END FUNCTIONS ###



# Extract user data
with open("user_data.json", "r") as file:
    user_data = json.load(file)


print("Personal Finance Tracker")


# LOGIN/SIGNUP
account_loop = True
while account_loop:
    choice_o = input("Login or signup? [l/s]: ").lower()

    # Login
    if choice_o == "l":
        name = input("Name: ")
        password = input("Password: ")
        not_found = True

        for user in user_data:
            # Account found
            if user == name:
                not_found = False
                if password == user_data[user]["password"]:
                    print("Account found.")
                    account_loop = False
                else:
                    print("Password incorrect.")
                    # Reset password
                    reset = input("Would you like to reset your password? [Y/n]: ").lower()

                    if reset == "y":
                        password = input("Enter your new password: ")
                        user_data[user]["password"] = password
                        print("Password succesfully reset.")
                        account_loop = False
        
        if not_found:
            print("Account not found.")

            

    # Signup
    elif choice_o == "s":
        # Make sure names are unique
        while True:
            name = input("Name: ")
            if name in user_data:
                print("Name already exists.")
            else:
                break

        password = input("Password: ")

        user_data[name] = {
            "password": f"{password}",
            "transactions": [],
            "category_budgets": {
                "bill": False,
                "food": False,
                "fun": False,
                "travel": False,
                "other": False
            }
        }

        print("User data added.")
        account_loop = False
    
    # Invalid choice
    else:
        print("Invalid choice")




# Main menu
flag = True
while flag:
    option = input("""\nEnter 1. Add transaction
      2. View remaining balance
      3. View all transactions
      4. View transactions by category
      5. Delete transaction
      6. Edit monthly category budgets
      7. View all monthly budgets
      0. Exit
Option: """)
    
    #[1] Add transaction
    if option == "1":
        
        # Name
        transact_name = input("Name of transaction: ")

        # Date
        while True:
            try:
                date_raw = input("\nDate (yyyy-mm-dd): ")

                date1 = calcDate(date_raw)
                date_final = str(date1)
                break

            except ValueError:
                print("Please enter a valid date")


        # Amount
        while True:
            try:
                amount = float(input("\nAmount: £"))
                break

            except ValueError:
                print("Please enter a valid amount")
        

        # Category
        category = chooseOption(["bill", "food", "fun", "salary", "travel", "other"], "Categories")
        

        # Type
        while True:
            transact_type = input("\nExpense or income? type one: ").lower()

            if transact_type == "expense" or transact_type == "income":
                break

            print("Please enter a valid type")
        

        # Frequency
        frequency = chooseOption(["one-time", "daily", "weekly", "monthly", "yearly"], "Frequencies")


        # Check if the budget has been exceeded
        budget = user_data[name]["category_budgets"][category]
        if budget:
            total_category_spending = calcCategorySpending(user_data[name]["transactions"], category)
            
            total_category_spending += amount
        
        
            print(f"\nTotal category spending: £{total_category_spending}")
            print(f"Total category budget: £{budget}")

            if budget < total_category_spending:
                print("WARNING: your budget has been exceeded")

        



        # Create and save final transaction
        transaction = {
            "transact_name": transact_name,
            "date": date_final,
            "amount": amount,
            "category": category,
            "type": transact_type,
            "frequency": frequency
        }

        user_data[name]["transactions"].append(transaction)
        print("\nTransaction succesfully added.")
    
    #[2] View remaining balance
    elif option == "2":
        # Time period
        time_period = chooseOption(["this week", "this month", "this year"], "Time period")

        # Get the date of the start and end of the time period
        start_of_time_period, end_of_time_period = getTimePeriodRange(time_period)
        

        # Calculate and display total balance at start of time period
        balance = balanceBeforeStart(start_of_time_period, user_data[name]["transactions"])

        print(f"\nBalance at the start of {time_period}: £{balance}")


        # Show transactions list and cumulate expenses within time period
        income_time_period, expense_time_period, transactions_list = balanceWithin(start_of_time_period, end_of_time_period, user_data[name]["transactions"])
        
        # Print transactions list
        print("\nTransactions within the time period:")

        for transaction in transactions_list:
            print(transaction)

        # Print cumulated amounts
        print(f"\nTotal income {time_period}: £{income_time_period}")
        print(f"Total expenses {time_period}: £{expense_time_period}")
   
        # Calculate balance at the end of the time period
        balance_time_period = income_time_period - expense_time_period
        balance += balance_time_period

        print(f"Balance at the end of {time_period}: £{balance}")


        # Calculate projected balance after 3 months

        projected_start, projected_end = getTimePeriodRange("next three months", end_of_time_period)

        print(f"\nPROJECTED BALANCE: transactions in the next 3 months ({projected_start} - {projected_end}):")

        projected_income, projected_expense, projected_transactions  = balanceWithin(projected_start, projected_end, user_data[name]["transactions"])

        # Print transactions list
        for transaction in projected_transactions:
            print(transaction)
        
        # Print cumulated amounts
        print(f"\nTotal income in the next 3 months: £{projected_income}")
        print(f"Total expenses in the next 3 months: £{projected_expense}")

        # Calculate balance after 3 months
        projected_balance = projected_income - projected_expense
        balance += projected_balance
        print(f"Balance after 3 months: £{balance}")


    #[3] View all transactions
    elif option == "3":
        printAllTransactions(user_data[name]["transactions"])


    #[4] View transactions by category
    elif option == "4":
        category = chooseOption(["bill", "food", "fun", "salary", "travel", "other"], "Categories")

        for transaction in user_data[name]["transactions"]:
            if transaction["category"] == category:
                printTransactDetails(transaction)
    

    #[5] Delete transaction
    elif option == "5":
        printAllTransactions(user_data[name]["transactions"])
        
        name_loop = True
        while name_loop:
            transaction_name = input("\nTransaction name: ")

            for i, t in enumerate(user_data[name]["transactions"]):
                if t["transact_name"] == transaction_name:
                    user_data[name]["transactions"].pop(i)
                    print("Transaction succesfully deleted.")
                    name_loop = False

            if name_loop:
                print("Transaction not found")
    

    #[6] Edit category budgets
    elif option == "6":
        category = chooseOption(["bill", "food", "fun", "travel", "other"], "Categories")
        current_category_budget = user_data[name]["category_budgets"][category]

        if current_category_budget:
            print(f"Current {category} budget: £{current_category_budget}")
        else:
            print(f"Current {category} budget: None")

        new_category_budget = float(input("Enter your new budget: £"))
        user_data[name]["category_budgets"][category] = new_category_budget
        print("Budget succesfully edited.")


    #[7] View all monthly budgets
    elif option == "7":
        for budget_name, budget in user_data[name]["category_budgets"].items():
            if budget:
                total_category_spending = calcCategorySpending(user_data[name]["transactions"], budget_name)
                print(f"\n{budget_name}: £{budget}")
                print(f"Total {budget_name} spending: £{total_category_spending}")

                if budget < total_category_spending:
                    print("WARNING: your budget has been exceeded")
            else:
                print(f"\n{budget_name}: None")


    #[0] Exit
    elif option == "0":
        flag = False


    #[X] Invalid choice
    else:
        print("Invalid choice")




try:
    with open("user_data.json", "w") as file:
        json.dump(user_data, file, indent=2)
except Exception as e:
    print(f"An error occurred: {e}")



