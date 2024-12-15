month_income = int(input("Enter your monthly income:"))
month_expenses = int(input("Enter your total monthly expenses:"))
monthly_saving = month_income - month_expenses
Projected_saving = monthly_saving * 12 + (monthly_saving * 12 * 0.05)
print("Your monthly saving are", f"${monthly_saving}")
print("Projected saving after one year, with interest, is:",f"${Projected_saving}")
