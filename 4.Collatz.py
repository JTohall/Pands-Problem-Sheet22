# Programme will ask user to input any positive integer and will output all the successive values.
# Using the collatz conjecture, the number (if even) will be divided by two, but if it is an odd number it will 
# be multiplied by three and add one. Each step is repeated until the final number is one. 

# Author: Jamie Tohall


number = int(input("Please enter a positive integer: "))
# Programme starts by asking the user to enter a positive integer


while number  !=1: 
# while loop - so the next value is returned until the number 1 is reached
    
# If the number is even (Able to be divided by 2 - '% 2') - divide by two and print
    if number % 2 == 0: 
        number = number //2
        
        print(number, end =' ')
            
# If the number returned in the sequence is odd - multiply it by three and add 1
# 3*number+1 is the sequence used to complete this calcualtion

    elif number % 2 == 1:
            number = 3*number+1
            
            print(number, end = ' ')
            