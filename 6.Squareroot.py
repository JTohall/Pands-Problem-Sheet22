# Write a programme that takes a postive floating point number and outputs an approximation
# of its square root
#Author: Jamie Tohall

Number = float(input("Please enter a positive number: "))

def SqRt (Number):
    
    approx = 0.5 * Number
    root = 0.5 * (approx+(Number/approx)) 
    
    while root !=approx:
        approx = root
        root = (approx+(Number/approx))/2
    
    return approx

print ("The square root of", Number,"is approximately {:.1f}".format(float(SqRt(Number))))