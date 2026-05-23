# Daily Expense Calculator

print("========== Daily Expense Calculator ==========\n")

# Taking inputs
daily_expense = float(input("Enter daily expense amount: ₹"))
days = int(input("Enter number of days: "))

# Calculating total expense
total_expense = daily_expense * days

# Displaying formatted output
print("\n==============================================")
print("              EXPENSE SUMMARY")
print("==============================================")
print(f"Daily Expense : ₹{daily_expense:.4f}")
print(f"Number of Days: {days}")
print("----------------------------------------------")
print(f"Total Expense : ₹{total_expense:.4f}")
print("==============================================")

# Thank you message
print("\nThank you for using the Expense Calculator!")