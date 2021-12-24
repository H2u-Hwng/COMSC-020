#
#   Use this program to test your class.

import clock

t1 = clock.Clock(18, 20)
t2 = clock.Clock(3, 47)

added = t1.add(t2)
subtract1 = t1.subtract(t2)
subtract2 = t2.subtract(t1)

print('Added is ', added)  # should print: Added is 2207
print('Subtract smaller is', subtract1) # should print: Subtract smaller is 1433
print('Subtract larger is', subtract2) # should print: Subtract larger is 1433

mil_string = input('Enter a military time in format hhmm or ENTER to quit: ')
while mil_string != '':
    am_pm_string = input('Enter a time in hh:mm AM/PM format: ')

    t1 = clock.from_military(mil_string)
    t2 = clock.from_am_pm(am_pm_string)
    t3 = t1.add(t2)
    t4 = t1.subtract(t2)
    print('Times are', t1, 'and', t2)
    print('Add result:', t3)
    print('Subtract result:', t4)
    print()

    mil_string = input('Enter a military time in format hhmm or ENTER to quit: ')
    
