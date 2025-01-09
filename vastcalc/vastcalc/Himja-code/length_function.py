# length function 

def length(n):
   
    count = 0
    for i in n:
        count += 1
    return count
n = input("enter the str here")
result = length(n)
print("the length of the str is", result)




