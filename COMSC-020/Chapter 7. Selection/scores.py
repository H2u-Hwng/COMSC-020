# scored.py
# Repeatedly read test scores (from 0 to 100), until the user
# enter -1 to finish. The input part of the program will ensure
# that the numbers are in the correct range.
# For each score, report the corresponding grade:
# 90-100 = A, 80-89 = B, 70-79 = C, 60-69 = D, < 60 = F
# When you have all the scores, report the number of scores
# entered, the total points and the average score.

# Display letter grade
def display_grade(score):
    if score >= 90:
        print("Congratulations! That is an A.")
    elif score >= 80:
        print("Good job. That is a B.")
    elif score >= 70:
        print("You are passing with a C.")
    elif score >= 60:
        print("Please study more. You have a D.")
    else:
        print("Sorry, that is an F.")


# Prompt user for score and returns score
def get_score():
    valid = False
    
    # Enter scores until a valid score is entered
    while not valid:
        score = float(input('Enter a score 0-100, or -1 to finish: '))
        
        # Check if valid score was entered
        if score == -1 or (score >=0 and score <= 100):
            valid = True
        else:
            print("Please enter a valid score.")
    
    return score


def main():
    
    # Intialize the count of scores and total scores
    count_scores = 0
    total_scores = 0
    
    # Keep entering scores until finished is set to true
    finished = False
    
    # Enter score until the user enters -1
    while not finished:
        score = get_score()
        
        # Check if user is finished entering scores
        if score == -1:
            finished = True
        else:
            # Display letter grade
            display_grade(score)
            
            # Update count of scores and total score
            count_scores += 1
            total_scores += score
            
    # Display number of scores, total score and average if scores were entered
    if count_scores > 0:
        average = total_scores / count_scores
        print(f"Total number of scores: {count_scores}")
        print(f"Total number of points: {total_scores:.1f}")
        print(f"Average score: {average:.2f}")
    else:
        print("No scores entered; no average computed.")
              
# Call main function
main()
