#
#   Ask for beginning amount, number of years,
#   and percent increase per year. Then make a loop
#   that prints out the money at each year.

amount = float(input('Starting amount of money: $'))
years = int(input('How many years do you want to accumulate interest? '))
percent = float(input('What is the annual interest rate in percent? '))

rate = percent / 100  # convert to decimal

for year in range(years):
    print("Year {}: you have ${:.2f}".format(year, amount))
    amount = amount + (rate * amount)
