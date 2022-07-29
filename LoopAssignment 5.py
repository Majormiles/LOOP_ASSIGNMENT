##Question 4 
##Write a program to find the factorial value of any number entered through the keyboard. 
##



# Python program to find.
# factorial of given number.
import math
def fact(n):
    return(math.factorial(n))
num = int(input("Enter the number:"))
f = fact(num)
print("Factorial of", num, "is", f)
