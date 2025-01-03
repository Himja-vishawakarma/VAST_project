import addition as A
import subtraction as S
import multiply as M
import division as D
import percentage as P
import square as SQ
import square_root as SQR
import modulus as MOD
import average as AVG

def calculator():
    print("Advanced Calculator")
    print("Operations: +, -, *, /, %, square, sqrt, mod, avg")

    while True:
        try:
            # Ask for the operation
            operation = input("Enter the operation you want to perform: ").lower()

            # Addition
            if operation == '+':

                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = A.add_numbers(num1, num2)
               
            # Subtraction
            elif operation == '-':

                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = S.subtract_numbers(num1, num2)
                

            # Multiplication
            elif operation == '*':

                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = M.multiply_numbers(num1, num2)
                
            # Division
            elif operation == '/':

                num1 = float(input("Enter the numerator: "))
                num2 = float(input("Enter the denominator: "))
                result = D.divide_numbers(num1, num2)
               

            # Percentage
            elif operation == '%':

                total_value = float(input("Enter the number: "))
                percentage_value = float(input("Enter the percentage: "))
                result = P.calculate_percentage(total_value, percentage_value)
                

            # Square
            elif operation == 'square':

                num = float(input("Enter the number to square: "))
                result = SQ.square_number(num)
               

            # Square Root
            elif operation == 'sqrt':

                num = float(input("Enter the number to find the square root of: "))
                result = SQR.square_root_number(num)
                

            # Modulus
            elif operation == 'mod':

                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = MOD.calculate_modulus(num1, num2)
                

            # Average
            elif operation == 'avg':
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = AVG.calculate_average(num1, num2)
                

            else:
                raise ValueError("Invalid operation!")

        except ValueError as e:
            print(f"Error: {e}")
        else:
            print(f"The result is: {result}")

        finally:
            # Ask if the user wants to continue
            continue_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if continue_calculation not in ['y','yes']:
                print("Thank you for using the calculator!")
                break

# Call the calculator function to run the program
calculator()
