def checkPalindrome(n):
    reverse = 0
    temp = n
    while temp != 0:    
        reverse = reverse * 10 + temp % 10
        temp = temp // 10
    if n == reverse:
        return True
    else:   
        return False
    
number = int(input("Enter a number for Palindrome : "))
if checkPalindrome(number):   
    print("Entered number is Palindrome")   
else:   
    print("Entered number is not Palindrome")

    