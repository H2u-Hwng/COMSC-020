# Part 1: Monthly Loan Payment.

p = int(input())
interest_rate = float(input())
r = interest_rate / (12 * 100)
number_of_years = int(input())
n = number_of_years * 12
monthly_payment = p * r * (1 + r)**n / ((1+r)**n - 1)
print(monthly_payment)

# Part 2: Minutes of Daylight.

