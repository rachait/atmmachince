import numpy as np

# Function to display the welcome message
def welcome_message():
    h = "WELCOME TO ATM"
    print(h.center(40))

# Function to display the menu options
def display_menu():
    print("\n1. WITHDRAW")
    print("2. DEPOSIT")
    print("3. BALANCE")
    print("4. TRANSACTION HISTORY")
    print("5. EXIT")

# Function to perform withdrawal
def withdraw(balance, transactions):
    try:
        w = float(input("Enter the amount to withdraw: "))
        if w > balance:
            print("Insufficient funds")
        else:
            balance -= w
            print(f"Amount withdrawn: {w}")
            transactions = np.append(transactions, [-w])
            if balance < 5000:
                print("Warning: Low balance")
    except ValueError:
        print("Invalid amount entered! Please enter a valid number.")
    return balance, transactions

# Function to perform deposit
def deposit(balance, transactions):
    try:
        ad = float(input("Enter the amount to deposit: "))
        balance += ad
        print(f"Amount deposited: {ad}")
        transactions = np.append(transactions, [ad])
        if balance < 5000:
            print("Warning: Low balance")
    except ValueError:
        print("Invalid amount entered! Please enter a valid number.")
    return balance, transactions

# Function to check balance
def check_balance(balance):
    print(f"Available Balance: {balance}")
    if balance < 5000:
        print("Warning: Low balance")

# Function to display transaction history
def show_transaction_history(transactions):
    if transactions.size == 0:
        print("No transactions yet.")
    else:
        print("Transaction History:")
        for i, t in enumerate(transactions, start=1):
            if t > 0:
                print(f"{i}. Deposit: {t}")
            else:
                print(f"{i}. Withdrawal: {-t}")

# Main ATM program logic
def atm_program():
    welcome_message()
    n = input("Enter account name: ")
    print(f"Hello {n}, Your Account Number is: 123456789")
    balance = 5000.0
    transactions = np.array([])  # Empty numpy array to store transaction history
    
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number corresponding to the options.")
            continue
        
        if choice == 1:
            balance, transactions = withdraw(balance, transactions)
        elif choice == 2:
            balance, transactions = deposit(balance, transactions)
        elif choice == 3:
            check_balance(balance)
        elif choice == 4:
            show_transaction_history(transactions)
        elif choice == 5:
            print("Thank you for using our ATM service!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Run the ATM program
atm_program()
