"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

p_a = 0.1
p_b = 0.15
s_min = 0
s_max = 1000

sales = float(input("Enter sales: $"))

while sales >= s_min:
    if sales >= s_max:
        bonus = sales * p_b
        print(f"Bonus:${bonus:.2f}")
        sales = float(input("Enter sales: $"))
    else:
        bonus = sales * p_a
        print(f"Bonus:${bonus:.2f}")
        sales = float(input("Enter sales: $"))
print("Invalid Number")
