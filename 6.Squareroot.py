# Write a programme that takes a positive floating point number and outputs an approximation of its square root
# Refer to the Newton method of estimating square roots and create a function called SqRt that does this.
# Author: Jamie Tohall

# Newtons method is a root finding algorithm which produces successively better approximations to the
# roots (or zeros) of a real valued function. 
# The idea is to start with an initial guess, then to approximate the function by its tangent line, and finally
# to compute the x-intercept of this tangent line. This x-intercept will typically be a better approximation
# to the original functions root than the first guess, and the method can be iterated. (Wikipedia.org)

# Newtons formula for finding the approximate square root of a number is -'root = 0.5 * (X + (N / X))' where X is any guess
# that can be assumed to be N or 1. 

Number = float(input("Please enter a positive number: "))
# Will firstly ask the user to input a positive number


def SqRt (Number):
# Creating the function SqRt to calculate the approximate square root of the input number
    
# Variables are set, using Newtons formula
    approx = 0.5 * Number
    root = 0.5 * (approx+(Number/approx)) 
    
# While loop is used 
    while root !=approx:
        approx = root
        root = (approx+(Number/approx))/2
        
  
    return approx

print ("The square root of", Number,"is approximately {:.1f}".format(float(SqRt(Number))))
# Will return the approximate square root of the number to one decimal place