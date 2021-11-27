# Constant for file name
INPUT_FILE = 'studentdata.txt'

def get_mean(data_list):
    ''' Take a data list and calculate its mean
        Return the mean of data list. '''
    
    # Determine the number having in the data list
    n = len(data_list)
    
    # Determine the sum of data in the data list
    sum_data = sum(data_list)
    
    # Check whether the data list is empty
    if n <= 0:
        mean = 0
    else:
        # Calculate the mean of the data list
        mean = sum_data / n
    
    return mean
    
    
def find_quantity(data_list):
    ''' Take a data list
        Return True if its length is larger than 6 and False otherwise. '''
    
    quantity = len(data_list) > 6
        
    return quantity
        
    
def main():
    ''' Define main function. '''
    
    # Open file and automatically close it when being done
    with open(INPUT_FILE, 'r') as input_file:
        for line in input_file:
            # Strip whitespace off the end and split student and scores
            student_scores = line.strip().split()
            
            # Determine the student's name
            student = student_scores[0]
            
            # Determine the scores list 
            scores = []
            for num in student_scores[1:]:
                scores.append(float(num))
            
            # Display student, minimum, maximum, and average
            print(f'Name: {student.capitalize()}')
            print(f'Minimum score: {min(scores)}; Maximum score: {max(scores)}')
            print(f'Average score: {get_mean(scores):,.3f}')
            
            # Check whether the student has more than six scores
            if find_quantity(scores):
                print('Having more than six quiz scores: YES')
            else:
                print('Having more than six quiz scores: NO')
            print()
            
# Call main function
main()
