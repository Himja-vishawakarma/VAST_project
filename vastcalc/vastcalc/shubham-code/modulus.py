def modulus(n1,n2):
    mod=(n1%n2)
    return mod
  
a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))

result=modulus(a,b)
print("The modulus of numbers is:", result)