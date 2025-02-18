

def division():
    
    try:
      
      num1 = int(input("Enter first number: "))
      num2 = int(input("Enter second number: "))

      result = num1//num2

      print("division of two number is: ", result)

    except:
       print("Invalid input,can't divide by zero: ")

    finally:
       print("division operation is completed")
       
division()
