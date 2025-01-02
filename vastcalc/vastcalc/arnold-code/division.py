# Function to divide two numbers
def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calling the function and printing the result
result = divide_numbers(num1, num2)
print(f"The result of dividing {num1} by {num2} is {result}")
