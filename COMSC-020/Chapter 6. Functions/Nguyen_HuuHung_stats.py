# Huu Hung Nguyen
# 10/11/2021
# Nguyen_HuuHung_stats.py
# The program contains 4 functions calculating reciprocal, arithmetic mean,
# geometric mean, and harmonic mean.
# It then displays results.

# Calculate and return reciprocal 
def reciprocal(num):
    
    # Calculate reciprocal
    reciprocal = 1 / num
    
    return reciprocal


# Calculate and return arithmetic mean
def mean(num1, num2, num3):
    
    # Calculate arithmetic mean
    arithmetic = (num1 + num2 + num3) / 3
    
    return arithmetic


# Calculate and return geometric mean
def geometric_mean(num1, num2, num3):
    
    # Calculate geometric mean
    geometric = (num1 * num2 * num3)**(1 / 3)
    
    return geometric


# Calculate and return harmonic mean
def harmonic_mean(num1, num2, num3):
    
    # Calculate harmonic mean
    harmonic = \
        reciprocal(mean(reciprocal(num1), reciprocal(num2), reciprocal(num3)))
    
    return harmonic
    
    
# Define main function
def main():
    
    # Display reciprocal
    print("Reciprocal of 8 is", reciprocal(8), "[should be 0.125]")
    print("Reciprocal of 4/3 is", reciprocal(4/3), "[should be 0.75]")
    print("Reciprocal of -3 is", reciprocal(-3), "[should be -0.3333...]")
    
    # Display arithmetic mean
    print("Mean of 1, 13, 4 is", mean(1, 13, 4), "[should be 6.0]")
    print("Mean of -5, -12, -9 is", mean(-5, -12, -9), "[should be -8.666...]")

    # Display geometric mean 
    print("Geometric mean of 144, 2, 6 is", geometric_mean(144, 2, 6), \
        "[should be 11.9999..]")
    print("Geometric mean of 2.1, 16.8, 16.8 is", geometric_mean(2.1, 16.8, 16.8), \
        "[should be 8.3999...]")
    
    # Display harmonic mean 
    print("Harmonic mean of 1, 2, 3 is", harmonic_mean(1, 2, 3), \
        "[should be 1.636363...]")
    print("Harmonic mean of -2, 1, 1 is", harmonic_mean(-2, 1, 1), \
        "[should be 2.0]")

# Call main function
main()