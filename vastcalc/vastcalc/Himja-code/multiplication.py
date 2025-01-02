## Multiplication

def multiplication(a,b,c):
  return a*b*c

try:

  n1 = int(input("Enter the first number here: "))
  n2 = int(input("Enter the second number here: "))
  n3 = int(input("Enter the third number here: "))

  product = multiplication(n1,n2,n3)
  print(f"{n1}x{n2}x{n3} is = ", (product))

except:
  print("Invalid input!! the given value is not an integer.")

finally:
  print("--Code is successfully executed.--")