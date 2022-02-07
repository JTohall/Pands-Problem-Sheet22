# My solution to weekly task 2
# Programme calulates users BMI
# Author: Jamie Tohall

height = int (input('Enter your height in cm:'))
weight = int (input( 'Enter your weight in Kg: '))

#Define the formula for calculating BMI
BMI = weight/(height/100)**2

print (f'Your BMI is {BMI}')

# add if elif statements to let user know where their results are on the BMI scale

if BMI <= 18.4: print ("You are underweight.")
elif BMI <= 24.9: print ("You are healthy.")
elif BMI <= 29.9: print ("You are overweight.")
elif BMI <= 34.9: print ("You are obese.")
elif BMI <= 39.9: print ("You are severely obese.")
elif BMI > 40: print ("you are mobidly obese.")
