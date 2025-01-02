# Function to calculate the average of two numbers
def calculate_average(a, b):
    return (a + b) / 2

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calling the function and printing the result
average = calculate_average(num1, num2)
print(f"The average of {num1} and {num2} is {average}\n")
