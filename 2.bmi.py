# Create a programme that calulates the users Body Mass Index (BMI)
# Author: Jamie Tohall

height = float(input('Enter your height in cm: '))
weight = float(input('Enter your weight in Kg: '))
# Will ask the user to enter their height in cm, then their weight in Kg, 'float' is used as the
# information the user will input will be a number, and could possibly be a floating point number.

BMI = weight/(height/100)**2
# Define the formula for calculating BMI

Result = "{:.2f}".format(BMI)
# After receiving feedback, I was asked to get the output result to two decimal places. I used string 
# format with {:.2f} to format the float to two decimal places

print (f'Your BMI is {Result}')
# Will print the users BMI

if BMI <= 18.4: print ("You are underweight.")
elif BMI <= 24.9: print ("You are healthy.")
elif BMI <= 29.9: print ("You are overweight.")
elif BMI <= 34.9: print ("You are obese.")
elif BMI <= 39.9: print ("You are severely obese.")
elif BMI > 40: print ("you are mobidly obese.")

# I added if/elif statements to let the user know where their results are on the BMI scale.
# This will for example give the user their BMI and let them know 'You are healthy', if their 
# result is below 24.9 and above 18.4.

