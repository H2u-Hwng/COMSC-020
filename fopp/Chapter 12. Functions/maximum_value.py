# Library
import random 

# Take list and return largest number by using sorted
def largest(lst):
    
    # Get largest number in list by using sorted
    lst_w_sorted = sorted(lst)
    largest_num = lst_w_sorted[-1]

    return largest_num


# Take list and return largest number by using max
def maximum(lst):
    
    # Get largest number in list by using max
    largest_num = max(lst)
    
    return largest_num


# Define main function
def main():
    
    # Creat a list
    lst = []
    for i in range(100):
        lst.append(random.randint(0, 1000))
    
    # Obtain largest number by using sorted
    print(largest(lst))
    
    # Obtain largest number by using max
    print(maximum(lst))
    
# Call main function
main()
