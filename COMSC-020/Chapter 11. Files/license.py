# Huu Hung Nguyen
# 11/09/2021
# Nguyen_HuuHung_license.py
# The program reads file named "correct_answers.txt".
# It compares between student's answers and correct answers in file.
# It then determines and displays the number of answering correctly,
# the number of answering incorrectly, and incorrectly answered questions.
# It also display that student pass or fail.

# Compare license answer and student answer
# Replace student incorrectly answer by "X"
# Return number correct answers, incorrect answers list,
# and post student answers list
def compare_answers(student_ans, license_ans, questions):
    num_correct_ans = 0
    incorrect_qns = []
    post_student_ans = []
    
    for n in range(len(license_ans)):
        # Check if student answer is correct or no
        if student_ans[n] == license_ans[n]:
            # Add one to the number correct asnwers
            num_correct_ans += 1
            # Add license answer to the end of the post student answers list
            post_student_ans.append(license_ans[n])
        else:
            # Add the incorrectly aswered question
            # to the end of the incorrect questions list
            incorrect_qns.append(questions[n])
            # Add "X" to the end of the post student answers list
            post_student_ans.append('X')
    
    return num_correct_ans, incorrect_qns, post_student_ans
    
    
# Define main function
def main():
    
    # Open "license_answers.txt" and automatically close it when being done
    with open('license_answers.txt', 'r') as license_office:
        license_qns = []
        license_ans = []
        
        for line in license_office:
            # Strip blanked space at both side and split question and answer
            question_answer = line.strip().split('.')
            
            # Add the question to the end of the license questions list
            license_qns.append(question_answer[0].strip())
            
            # Add the correct answer to the end of the license answers list
            license_ans.append(question_answer[1].strip())
            
    # Open "student_answers.txt" and automatically close it when being done
    with open('student_answers.txt', 'r+') as student:
        student_ans = []
        
        for line in student:
            # Strip blanked space at both side and split question and answer
            question_answer = line.strip().split('.')
            
            # Add the student answer to the end of the student answers list
            student_ans.append(question_answer[1].strip())
        
        # Get number correct answer, incorrectly answered questions, 
        # and post student answers
        num_correct_ans, incorrect_qns, post_student_ans = \
                        compare_answers(student_ans, license_ans, license_qns)
        
    
        # Clear the contents of the file
        student.truncate(0)
        # Move to the beginning of the file
        student.seek(0)
    
        for n in range(1, len(license_ans) + 1):
            student.write(f'{n}. {post_student_ans[n - 1]} \n')

    # Display results
    print(f'You answered correctly {num_correct_ans} questions.')
    print(f'You answered incorrectly {len(incorrect_qns)} questions.')
    
    # Check if all answers are correct
    if len(incorrect_qns) == 0:
        print('There are no incorrectly answered questions.')
    else:
        incorrect_qns_format = ', '.join(incorrect_qns)
        print(f'Incorrectly answered questions are {incorrect_qns_format}.')
            
    # Check if students pass or no
    if num_correct_ans >= 15:
        print('You pass the exam!')
    else:
        print('You fail the exam!')

# Call main function
main()