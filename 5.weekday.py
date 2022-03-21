# Programme will output what day of the week it is
# Author: Jamie Tohall

# Import datetime module
import datetime

# Define day
day = datetime.datetime.today().weekday()

# Each weekday in python datetime is represented by a number, Monday = 0, 
# Tuesday = 1 etc. 

if day <5: print("Unfortunately today as a weekday :(")
# Therefore if the day is less than 5 (Saturday) It will be a weekday.

else: print("It's the weekend, yay!")
# other two options will be Saturday and Sunday, or 5 & 6, so we know it will be the weekend.






