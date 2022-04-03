# Programme will let the user know if its a weekday or the weekend 
# Author: Jamie Tohall

# Import datetime module
import datetime

# Define day
day = datetime.datetime.today().weekday()

# Each weekday in python datetime is represented by a number, Monday = 0, Tuesday = 1 etc. 
# Therefore if the day is less than 5 (Saturday) It will be a weekday.
if day <5: print("Unfortunately today is a weekday :(")

else: print("It's the weekend, yay!")
# Other two options will be Saturday and Sunday, or 5 & 6, so we know it will be the weekend.
