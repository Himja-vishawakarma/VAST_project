# calculator functionality which takes 3 inputs 
n1= int(input("Enter the first number: "))
n2= int(input("Enter the second number: "))
n3= int(input("Enter the third number: "))


print("Type 1 for addition ")
print("Type 2 for subtraction")
print("Type 3 for multiplication")

i= int(input("Enter operation of your choice: "))

if i== 1:
    print("Addition of",f"{n1}+{n2}+{n3}", n1+n2+n3)
elif i==2:
    print("Subtraction of",f"{n1}-{n2}-{n3}", n1-n2-n3)
    
elif i==3:
    print("Multiplication of",f"{n1}*{n2}*{n3}", n1* n2*n3 )

else:
    print("Please enter a valid input")