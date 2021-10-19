# Find how many numbers from 1 to 1000 are multiples of 7 or 5.

# Constants for first_num and last_num
FIRST_NUM = 1
LAST_NUM = 1000

# Return number of multiples of 7 or 5 from first_num to last_num
def get_multiples(first_num, last_num):
    
    # Initialize count of multiples
    count_multiples = 0
    
    # Count number of multiples of 7 or 5
    for n in range(first_num, last_num + 1):
        if n % 7 == 0 or n % 5 == 0:
            count_multiples += 1
            
    return count_multiples
            
            
# Define main function
def main():
    
    # Obtain number of multiples of 7 or 5 from 1 to 1000
    multiples = get_multiples(FIRST_NUM, LAST_NUM)

    # Display result
    print(f'There are {multiples} multiples of 7 or 5 from 1 to 1000.')

# Call main function
main()