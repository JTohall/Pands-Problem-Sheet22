# Programme will ask user to input any positive integer and will output all the successive values.
# Using the collatz conjecture, the number (if even) will be divided by two, but if it is an odd number it will 
# be multiplied by three and add one. Each step is repeated until the final number is one. 

# Author: Jamie Tohall


number = int(input("Please enter a positive integer:"))


# while loop - so the next value is returned until the number 1 is reached
while number  >1: 
    
# If the number is even - divide by two
    if number % 2 == 0: 
        print(number//2)
        number = number //2
            
# If the number is odd - multiply by three and add 1. 
    elif number % 2 == 1:
            print(3*number+1)
            number = 3*number+1
            
# Programme also works if an odd integer is entered. I wasn't sure how to add a ValueError return
# for an odd number.