def tip_calculator():
    print("Welcome to the Tip Calculator!")

    try:
        bill_amount = float(input("Enter the bill amount: $"))
        if bill_amount < 0:
            print("Bill amount cannot be negative.")
            return

        tip_percentage = float(input("Enter the tip percentage (e.g., 10 for 10%): "))
        if tip_percentage < 0:
            print("Tip percentage cannot be negative.")
            return

        tip_amount = (bill_amount * tip_percentage) / 100
        total_amount = bill_amount + tip_amount

        print(f"\nBill Amount: ${bill_amount:.2f}")
        print(f"Tip Percentage: {tip_percentage}%")
        print(f"Tip Amount: ${tip_amount:.2f}")
        print(f"Total Amount: ${total_amount:.2f}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    tip_calculator()

