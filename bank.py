# 🏦 Project Title: Advanced Bank ATM System
# 📌 Objective:
# Students will build a fully functional ATM system using Python that allows users to:
# ✅ Check their balance
# ✅ Deposit money (No negative deposits)
# ✅ Withdraw money (Check for sufficient balance)
# ✅ View transaction history
# ✅ Use a PIN for security
# ✅ Exit the system


# 📌 Requirements:
# 1. welcome message and action to continue
# 2. enter pin to continue to the ATM- 4 digit pin - numbers only
# 3. Display the menu
# 4. check balance againt an initial balance of 1000.00
# 5. deposit money - no negative deposits      
# 6. Withdraw money -check for sufficient balance
# 7. View transaction history (checking deposit and withdraw)
# 8. Exit the system

PIN = "1234"
balance = 1000.00


#checking balance
def check_balance():
    print(f"Your balance is {balance}")


# Deposit 
def deposit(balance):
    try:
        amount = float(input("How much do u want to deposit: "))
    
        if amount < 0:
            print("invalid amount")
        else:
            balance =+ amount
        
        return balance
    except Exception as e:
        print("something went wrong: " + e)


# Withdraw Money
def withdraw(balance):
    try:
        amount = float(input("How much do u want to withdraw: "))
    
        if amount > balance:
            print("insuffient bal")
        elif amount < 0:
            print("invalid amount")
        else:
            balance = balance - amount
        
        return balance
    except Exception as e:
        print("something went wrong: " + e)





# pin = input("Welcome to the ATM. Your Money is Safe with Us\n Enter your 4 digit pin to continue\n")


# if pin != PIN:
#     print("Invalid Pin. Please try again")
#     pin = input("Enter your correct 4 digit pin to continue\n")




# else:
#     menu =     '''1. Check Balance
#     2. Deposit Money
#     3. Withdraw Money
#     4. View Transaction History
#     5. Exit the System'''


#     print(menu)
#     choice = int(input("Enter your choice\n"))


#     if choice == 1:
#         print(f"Your balance is {balance}")
