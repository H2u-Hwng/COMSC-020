# Huu Hung Nguyen
# 10/08/2021
# Nguyen_HuuHung_stats.py
# 

# Define reciprocal function
def reciprocal(a):
    
    # Calculate reciprocal
    reciprocal = 1 / a
    
    return reciprocal

# Define mean function
def mean(a, b, c):
    
    # Calculate average
    average = (a + b + c) / 3
    
    return average

# Define geometric mean function
def geometric_mean(a, b, c):
    
    # Calculate geometric
    geometric = (a * b * c)**(1/3)
    
    return geometric

# Define harmonic mean function
def harmonic_mean(a, b, c):
    
    # Calculate harmonic
    harmonic = 3 / (reciprocal(a) + reciprocal(b) + reciprocal(c))
    
    return harmonic
    
# Define main function
def main():
    
    # Call reciprocal function
    print("Reciprocal of 8 is", reciprocal(8), "[should be 0.125]")
    print("Reciprocal of 4/3 is", reciprocal(4/3), "[should be 0.75]")
    print("Reciprocal of -3 is", reciprocal(-3), "[should be -0.3333...]")
    
    # Call mean function
    print("Mean of 1, 13, 4 is", mean(1, 13, 4), "[should be 6.0]")
    print("Mean of -5, -12, -9 is", mean(-5, -12, -9), "[should be -8.666...]")

    # Call geometric mean function
    print("Geometric mean of 144, 2, 6 is", geometric_mean(144, 2, 6), \
        "[should be 11.9999..]")
    print("Geometric mean of 2.1, 16.8, 16.8 is", geometric_mean(2.1, 16.8, 16.8), \
        "[should be 8.3999...]")
    
    # Call harmonic mean function
    print("Harmonic mean of 1, 2, 3 is", harmonic_mean(1, 2, 3), \
        "[should be 1.636363...]")
    print("Harmonic mean of -2, 1, 1 is", harmonic_mean(-2, 1, 1), \
        "[should be 2.0]")

# Call main function
main()
