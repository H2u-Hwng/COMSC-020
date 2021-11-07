# Counting words having length 5 and return count 
def count_words(words):
    
    # Initialize count
    count = 0
    
    for w in words:
        # Check if length of word is 5
        if len(w) == 5:
            count += 1
            
    return count


# Define main function
def main():
    
    # Prompt user for a sentence
    sentence = input("Please enter a sentence: ")
    
    # Initialize words list
    words_list = sentence.split()
    
    # Obtain counting
    counting = count_words(words_list)
    
    # Display result
    print(f'There are {counting} words in "{sentence}" having length 5.')
    
# Call main function
main()
