
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly income: "))
monthly_savings = monthly_income-monthly_expenses
annual_savings = monthly_income * 12 
projected_savings= annual_savings + (annual_savings * 0.05)
print(f"Your monthly saving are ${monthly_savings:.2f}")
print(f"Projected saving after one year, with interest, is: ${projected_savings:2f}")