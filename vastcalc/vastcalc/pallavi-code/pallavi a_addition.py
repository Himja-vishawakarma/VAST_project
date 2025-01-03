def calculate_sum(a, b, c):
    return a + b + c

try:
    a = float(input("Enter the number a = "))
    b = float(input("Enter the number b = "))
    c = float(input("Enter the number c = "))
    sum = calculate_sum(a, b, c)
    print("Sum of three numbers =", sum)
except :
    print("enter numeric values.")
finally:
    print("Program executed successfully.")



