# Bank System - Python Project
# Created by Ishimwe Gilbert

accounts = {}


def create_account():
    name = input("Enter your name: ")
    account_number = input("Create account number: ")

    if account_number in accounts:
        print("Account already exists!")
    else:
        accounts[account_number] = {
            "name": name,
            "balance": 0
        }
        print("Account created successfully!")


def deposit_money():
    account_number = input("Enter account number: ")

    if account_number in accounts:
        amount = float(input("Enter amount to deposit: "))

        if amount > 0:
            accounts[account_number]["balance"] += amount
            print("Money deposited successfully!")
        else:
            print("Invalid amount!")

    else:
        print("Account not found!")


def withdraw_money():
    account_number = input("Enter account number: ")

    if account_number in accounts:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= accounts[account_number]["balance"]:
            accounts[account_number]["balance"] -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")

    else:
        print("Account not found!")


def check_balance():
    account_number = input("Enter account number: ")

    if account_number in accounts:
        balance = accounts[account_number]["balance"]
        print("Your balance is:", balance)

    else:
        print("Account not found!")


def main():

    while True:
        print("\n===== BANK SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            deposit_money()

        elif choice == "3":
            withdraw_money()

        elif choice == "4":
            check_balance()

        elif choice == "5":
            print("Thank you for using Bank System!")
            break

        else:
            print("Invalid choice!")


main()
