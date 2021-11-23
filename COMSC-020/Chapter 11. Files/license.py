# Huu Hung Nguyen
# 11/19/2021
# Nguyen_HuuHung_license.py
# The program reads file named "student_answers.txt".
# It compares between student's answers and correct answers.
# It displays that student passed or failed.
# It then determines and displays the number of answering correctly,
# the number of answering incorrectly, and incorrectly answered questions.

# Constants for correct answers, passing and input file
CORRECT_ANSWERS = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
                   'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A'] 
PASS = 15
INPUT_FILE = 'student_answers.txt'

def grade_student(answers):
    '''Take a student's answers and grade them based on correct answers
       Return the incorrect questions.'''
    
    # Initialize the incorrect questions list
    incorrect_questions = []
    
    for n in range(len(CORRECT_ANSWERS)):
        # Check whether the answer is incorrect
        if answers[n] != CORRECT_ANSWERS[n]:
            # Add question to the end of the incorrect questions list
            incorrect_questions.append(str(n + 1))

    return incorrect_questions
    
    
def main():
    '''Define main function.'''
    
    # Open file and automatically close it when being done
    with open(INPUT_FILE, 'r') as input_file:
        
        # Initialize student answers list
        student_answers = []
        
        # Create a list of student answers
        for line in input_file:
            # Strip the whitespace off the end
            # Add the answers to the end of the student answers list
            student_answers.append(line.strip())
        
        # Determine the incorrect questions
        incorrect_questions = grade_student(student_answers)
        
        # Determine the number of questions, incorrect and correct answers
        num_questions = len(CORRECT_ANSWERS)
        num_incorrect = len(incorrect_questions)
        num_correct = num_questions - num_incorrect
        
        # Check if the student passed or failed
        if num_correct >= PASS:
            print('congratulations! You passed the exam.')
        else:
            print('Sorry, you failed the exam.')
        
        # Display the numbers of correct and incorrect answers
        print(f'You answered correctly {num_correct} questions.')
        print(f'You answered incorrectly {num_incorrect} questions.')
        
        # Display the wrong questions
        if num_incorrect == 0:
            print('There are no incorrectly answered questions.')
        else:
            incorrect_questions = ', '.join(incorrect_questions)
            print(f'Incorrectly questions: {incorrect_questions}.')
                          
# Call main function
main()
