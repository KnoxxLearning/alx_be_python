#monthly_income = input("Enter your monthly income: ")

#now I need to make sure that the input accepted is the right data type, what's the right data type for money? 

monthly_income = float(input("Enter your monthly income: "))

monthly_expenses = float(input("Enter your total Monthly Expenses: "))

monthly_savings = monthly_income - monthly_expenses
print("Your monthly savings are $",monthly_savings)

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Projected savings after one year, with interest, is:$",projected_savings)