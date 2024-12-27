
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Before swapping:")
print(f"a = {a}, b = {b}")
temp = a
a = b
b = temp
print("After swapping:")
print(f"a = {a}, b = {b}")