balance=5000

while True:
    choice = input("Enter choice (1-Deposit, 2-Withdraw, 3-Exit): ")

    match choice:
        case "1":
            amount = float(input("How much do you want to deposit? "))
            balance += amount
            print(f"You deposited ₹{amount}. Your new balance is ₹{balance}")

        case "2":
            amount = float(input("How much do you want to withdraw? "))
            if amount <= balance:
                balance -= amount
                print(f"You withdrew ₹{amount}. Your new balance is ₹{balance}")
            else:
                print("Insufficient funds")

        case "3":
            print("Thank you for banking with us!")
            break

        case _:
            print("Invalid choice")
