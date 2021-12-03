# Huu Hung Nguyen
# 12/02/2021
# Nguyen_HuuHung_lentest.py
# The program imports all the functions defined in Nguyen_HuuHung_lens.py
# It prompts the user for the information of two lens
# and calculate the lens f stop of two lens.
# It then display the information and lens f stop of two lens
# and checks whether two lens are the same.

# Import all the functions defined in Nguyen_HuuHung_lens.py
from lens import Lens

def main():
    ''' Define main function. '''
    
    # Prompt the user for the first lens' focal length and aperture
    focal_length1 = float(input('Enter focal length of first lens in mm: '))
    aperture1 = float(input('Enter aperture of first lens in mm: '))
    
    print()
    
    # Prompt the user for the second lens' focal length and aperture
    focal_length2 = float(input('Enter focal length of second lens in mm: '))
    aperture2 = float(input('Enter aperture of second lens in mm: '))
    
    print()
    
    # Determine the first lens and display its information
    lens1 = Lens(focal_length1, aperture1)
    print(f'First lens: {lens1}; f-stop {lens1.calc_f_stop():.1f}')
    
    # Determine the second lens and display its information
    lens2 = Lens(focal_length2, aperture2)
    
    # Check whether the second lens is the same as the first lens
    if lens2 == lens1:
        print('The second lens is the same as the first one.')
    else:
        print(f'Second lens: {lens2}; f-stop {lens2.calc_f_stop():.1f}')
        
# Call main function
main()
