# Huu Hung Nguyen
# 11/27/2021
# Nguyen_HuuHung_clocktest.py
# The program imports all the functions defined in clock.py.
# It repeatedly prompts the user to enter a time in military format
# and in AM/PM format, separated by a comma until the user presses ENTER.
# It then determines and displays two clock objects, the sum
# and difference of the times.

# Import all the functions defined in clock.py
from clock import Clock, to_minutes, from_military, from_am_pm

def main():
    ''' Define main function. '''
    
    again = True
    
    # Repeatedly ask the users until they press ENTER
    while again:
        # Prompt the user for the military time and AM/PM time
        input_prompt = 'Enter military time and AM/PM time, ' + \
                       'separated by a comma, \n' + \
                       'or just press ENTER to quit: '
        times = input(input_prompt)
        
        # Check whether the user presses ENTER
        if times == '':
            again = False
        else:
            # Determine and display two clock objects from the user’s string
            times_list = times.split(',')
            
            military_time = from_military(times_list[0])
            am_pm_time = from_am_pm(times_list[1])
            print(f'You entered {military_time} and {am_pm_time}')
            
            # Add the two times and display the sum of the times
            sum_times = military_time.add(am_pm_time)
            print(f'The sum of the times is {sum_times}')
            
            # Subtract the two times and display the difference of the times
            diff_times = military_time.subtract(am_pm_time)
            print(f'The difference of the times is {diff_times} \n')
                   
# Call main function
main()