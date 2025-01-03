def division(n1, n2):
    
    try:
        result=(n1//n2)
        print("The division of the two numbers is:", result)
        
    except:
        print( "Error: Division by zero is not allowed.")
    
    finally:
        print("The division operation is complete.")
  
a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))

division(a,b)
