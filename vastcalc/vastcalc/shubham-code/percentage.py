def percentage(n1, n2):
    per=(n1*n2)/100
    return per
  
a=int(input("Enter the value:"))
b=int(input("Enter the % value:"))

result=percentage(a,b)
print("The percentage of the numbers is:", result)