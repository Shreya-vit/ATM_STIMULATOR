
#                    ATM SIMULATOR


balance = 10000
pin = "1234"
transaction_history = []
print("====================================")
print("          WELCOME TO ATM")
print("====================================")

# PIN Verification
for attempt in range(3):
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin == pin:
        print("\nLogin Successful!")
        break
    else:
        print("Incorrect PIN.")

else:
    print("\nToo many incorrect attempts.")
    print("Your card has been blocked.")
    exit()

# ATM Menu
while True:
    print("\n====================================")
    print("              ATM MENU")
    print("====================================")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Transaction History")
    print("6. Exit")
    print("====================================")

    choice = input("Enter your choice: ")

    # 1. Check Balance
    if choice == "1":
        print(f"\nYour current balance is: ₹{balance}")

    # 2. Deposit
    elif choice == "2":
        try:
            amount = float(input("Enter amount to deposit: ₹"))

            if amount > 0:
                balance += amount
                transaction_history.append(
                    f"Deposited ₹{amount:.2f}"
                )
                print(f"₹{amount:.2f} deposited successfully.")
                print(f"New balance: ₹{balance:.2f}")
            else:
                print("Enter a valid amount.")

        except ValueError:
            print("Please enter a valid number.")

    # 3. Withdraw
    elif choice == "3":
        try:
            amount = float(input("Enter amount to withdraw: ₹"))

            if amount <= 0:
                print("Enter a valid amount.")

            elif amount > balance:
                print("Insufficient balance.")

            else:
                balance -= amount
                transaction_history.append(
                    f"Withdrawn ₹{amount:.2f}"
                )
                print(f"Please collect your cash: ₹{amount:.2f}")
                print(f"Remaining balance: ₹{balance:.2f}")

        except ValueError:
            print("Please enter a valid number.")

    # 4. Change PIN
    elif choice == "4":
        old_pin = input("Enter your current PIN: ")

        if old_pin == pin:
            new_pin = input("Enter new 4-digit PIN: ")

            if len(new_pin) == 4 and new_pin.isdigit():
                confirm_pin = input("Confirm new PIN: ")

                if new_pin == confirm_pin:
                    pin = new_pin
                    print("PIN changed successfully.")
                else:
                    print("PINs do not match.")
            else:
                print("PIN must contain exactly 4 digits.")

        else:
            print("Incorrect current PIN.")

    # 5. Transaction History
    elif choice == "5":
        print("\n========== TRANSACTION HISTORY ==========")

        if len(transaction_history) == 0:
            print("No transactions yet.")
        else:
            for transaction in transaction_history:
                print("-", transaction)

        print("=========================================")

    # 6. Exit
    elif choice == "6":
        print("\nThank you for using our ATM.")
        print("Have a nice day!")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please select 1-6.")
