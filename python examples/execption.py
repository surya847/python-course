import sys

print ("Lets fix the previous code with exception handling")

try:
    number = int(input("Enter a number between 1 - 10 "))

except ValueError:
    print ("Err.. numbers only")
    sys.exit()

print( "you entered number ", number)