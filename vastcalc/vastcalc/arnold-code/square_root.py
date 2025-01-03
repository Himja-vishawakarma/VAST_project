import math

# Function to calculate the square root
def calc_sq_root(number):
    if number < 0:
        return "Cannot calculate the square root of a negative number"
    return math.sqrt(number)

# # Take input from the user
# number = float(input("Enter a number to find its square root: "))

# # Calculate and display the square root
# result = calc_sq_root(number)
# print(f"The square root of {number} is {result}")
