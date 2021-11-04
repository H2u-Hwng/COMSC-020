# Library
import random

# Initialize randlist
randlist = []

for _ in range(100):
  
    # Append random number between 0 and 1000
    randlist.append(random.randint(0, 1000))
    
# Display randlist
print(randlist)
