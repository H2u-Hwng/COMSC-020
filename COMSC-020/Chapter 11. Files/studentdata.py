# Open file
student_data = open('studentdata.txt', 'r')

for name_scores in student_data:
    name_scores_list = name_scores.split()
    # Check if students have more than six quiz scores
    if len(name_scores_list[1:]) > 6:
        # Display names of students having more than six quiz scores
        print(name_scores_list[0])
        
# Close file
student_data.close()
