
def addition():
    
    try:
      
      num1 = int(input("Enter first number: "))
      num2 = int(input("Enter second number: "))

      result = num1 + num2

      print("addition of two number is: ", result)

    except:
       print("Invalid input,plzz enter numeric values: ")

    finally:
       print("addition operation is completed")
       
addition()