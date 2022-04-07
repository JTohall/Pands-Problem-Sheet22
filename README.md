# **Pands Problem Sheet**
<br/>

#### Author: Jamie Tohall
#### Student Number: G00411380
<br/>

#### Module: Programming and Scripting
#### Lecturer: Andrew Beattie
#### Submission Date: 29th April 2022
<br/>
<br/>


__________________________________________________________________________________________________________________________________________________________
## Task 2 - BMI.py
<br/>

> Write a programme that calculates somebody's Body Mass Index (BMI).

<br/>

This was the first assigned weekly task. After completing week two lectures and labs, as well as doing my own research, I found the programme straightforward.
I added the 'If/Elif' statements after seeing them in 'Wrt Tech's video on creating a BMI calculator. I thought it was a good idea to add some extra feedback in the output, letting the user know what weight range they are in as well as their BMI score, but it also gave me some experience in using If/Elif statements. <br/>
I received feedback on my weekly tasks from Andrew in week 7 and it was suggested that I get the output to two decimal places. I used the "str.format()" with "{:.2f}" to print the float with two decimal places. I was not familiar with this string format in week two, but I used it in my week six task 'Squareroot', so I had an idea how to solve this. 

<br/>

### References

[1] Github.com (How to calculate BMI of a person for info) - https://secondminute.github.io/how-to-calculate-bmi-of-a-person/

[2] youtube.com (Python - BMI calculator (Wrt Tech)) - https://www.youtube.com/watch?v=g9jO0kKnZT0

[3] W3schools.com (Python If... Else) https://www.w3schools.com/python/python_conditions.asp

[4] Pythonguides (Python Print to Two Decimal Places) - https://pythonguides.com/python-print-2-decimal-places/#:~:text=In%20Python%2C%20to%20print%202%20decimal%20places%20we,will%20print%20the%20float%20with%202%20decimal%20places.

<br/>

__________________________________________________________________________________________________________________________________________________________
## Task 3 - Secondstring.py
<br/>

> Write a programme that asks a user to input a string and outputs every second letter in reverse order.

<br/>

This programme starts by asking the user to 'Please input a sentence:', and defines the input as 'Sentence'. To print the sentence in reverse order with every second letter missing, the slicing syntax ```[::-2]``` is used. The -2 will extract every second letter. 

<br/>

### References

[1] w3schools.com (How to reverse a String in Python) - https://www.w3schools.com/python/python_howto_reverse_string.asp

[2] Realpython.com (Reverse Strings in Python: Reversed(), Slicing, and more) - https://realpython.com/reverse-string-python/

[3] Geeksforgeeks.org (String Slicing in Python) - https://www.geeksforgeeks.org/string-slicing-in-python/

[4] Pythonforbeginners.com (String Slicing in Python) -  https://www.pythonforbeginners.com/strings/string-slicing-in-python

<br/>

__________________________________________________________________________________________________________________________________________________________
## Task 4 - Collatz.py
<br/>

> Write a programme that asks the user to input any positive integer and outputs the successive values of the following calculation.
> At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
> Have the programme end if the current value is one.

<br/>

"The Collatz conjecture in mathematics asks whether repeating two simple arithmetic operations will eventually transform every positive integer into one. It concerns sequences of integers in which each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that these sequences always reach 1, no matter which positive integer is chosen to start the sequence." (Wikipedia)

<br/>

I start the programme by asking the user to input a positive integer, using the int() function to convert the given value into an integer. I used the while loop, so a number is continiously returned until the value is 1, using the command ```"While number !:1"```. In accorance with the Collatz Conjecture, if the number is positive, it will then be divided by two. I used an 'If' statement and entered the command of ```'If number %2==0: number=number//2```. If a number in the sequence or the number inputted by the user is an odd number, it will be multiplied by three and add one. Therefore I used the following 'Elif' statement ```elif number %2==1: number=3*number+1```, which will execute the conjecture. Both If anf Elif statments are followed by the print command ```print(number, end =' ')``` so the output will be following Collatz sequence from the number 10 printed on the same line. If for example the input number was 10, the programme output would look like: ```5 16 8 4 2 1```. 

<br/>

### References

[1] Youtube.com (The Simplest Math Problem No One Can Solve - Collatz Conjecture (Veritasium)) - https://www.youtube.com/watch?v=094y1Z2wpJg

[2] Stackoverflow.com (Collatz Conjecture in Python) -  https://stackoverflow.com/questions/46505460/collatz-conjecture-in-python

[3] Pythonpool.com (Understanding Collatz Sequence in Python) - https://www.pythonpool.com/collatz-sequence-python/

[4] Geeksforgeeks.com (Programme to Print Collatz Sequence) -  https://www.geeksforgeeks.org/program-to-print-collatz-sequence/

[5] Youtube.com (Collatz Conjecture in Python (MartinBuildsFromSource)) -  https://www.youtube.com/watch?v=wmvHTQhkBq4

[6] Youtube.com (Collatz Sequence Algorithm in Python (StudentEngineer) - https://www.youtube.com/watch?v=lAp_5qTdOhM

<br/>

__________________________________________________________________________________________________________________________________________________________
## Task 5 - Weekday.py
<br/>

> Write a programme that outputs whether or not today is a weekday. 

<br/>

### References

[1] Stackoverflow.com (Questions) - https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python

[2] Geeksforgeeks.org (Python dateTime Weekday() Method with Example) - https://www.geeksforgeeks.org/python-datetime-weekday-method-with-example/

[3] Pythonic.com (Weekday Function in Python) -  https://pythontic.com/datetime/date/weekday

[4] W3schools.com (Python DateTime) - https://www.w3schools.com/python/python_datetime.asp

<br/>

__________________________________________________________________________________________________________________________________________________________
## Task 6 - Squareroot.py
<br/>

> Write a programme that takes a positive floating-point number as input and outputs an approximation of its square root. You should create a function called SqRt 
> that does this. I am asking you to create your own square root function and I suggest you look at the Newton Method at estimating square roots.

<br/>

### References

[1] Stackoverflow.com (Writing your own Square Root Function) - https://stackoverflow.com/questions/1623375/writing-your-own-square-root-function

[2] Geeksforgeeks.org (Find Root of a Number using Newtons Method) - https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

[3] Handlebar-online.com (How do you write a Square Root Program in Python?) - https://www.handlebar-online.com/articles/how-do-you-write-a-square-root-program-in-python/

[4] Positronx.io (How to find the Square Root in Python?) -  https://www.positronx.io/find-square-root-in-python/#:~:text=In%20the%20first%20example%2C%20we%20are%20going%20to,sqrt%20%3D%20num%20%2A%2A%200.5%20print%28%22square%20root%3A%22%2C%20sqrt%29

[5] Math.Mit.Edu (Square Roots via Newtons Method) - https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf

[6] Tutorialsinhand.com (Python Programme to find Square Root of a Number by Newtown's Method) - https://tutorialsinhand.com/Articles/python-program-to-find-square-root-of-a-number-using-newton-square-root-formula.aspx#:~:text=%F0%9F%92%BB%20Program%20For%20finding%20Square%20root%20using%20Newton%27s,%28approx_root%20%2B%20n%2Fapprox_root%29%20approx_root%20%3D%20betterapprox%20return%20betterapprox

<br/>

__________________________________________________________________________________________________________________________________________________________
## Task 7 - Es.py
<br/>

> Write a programme that reads in a text file and outputs the number of e's it contains. Think about what is being asked here and document any assumptions you are making. The programme should take the filename from an argument on the command line. 

<br/>

### References

[1] Askpython.com (Python Command Line Arguments) - https://www.askpython.com/python/python-command-line-arguments

[2] Javapoint.com (Python Sys Module) - https://www.javatpoint.com/python-sys-module

[3] Simplilearn.com (Count in Python - All you Need to Know About It) - https://www.simplilearn.com/tutorials/python-tutorial/count-in-python#:~:text=The%20count%20%28%29%20method%20is%20one%20of%20the,and%20the%20number%20of%20cells%20contains%20numbers%20too.

[4] Pythonexamples.org (Python - Count Occurrences of a Word in Text File) - https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/

<br/>

__________________________________________________________________________________________________________________________________________________________
## Task 8 - Plottask.py
<br/>

> Write a programme that displays a plot of the functions f(x)=x, g(x)=x2, h(x)=x3 in the range [0,4] on the one set of axes. 

<br/>

### References

[1] W3schools.com (Matplotlib Tutorial) - https://www.w3schools.com/python/matplotlib_intro.asp

[2] Realpython.com (Python Plotting with Matplotlib (Guide)) - https://realpython.com/python-matplotlib-guide/#a-burst-of-color-imshow-and-matshow

[3] Realpython.com (Plot with Pandas: Python Data visualization for Beginners) - https://realpython.com/pandas-plot-python/

[4] W3schools.com (Matplotlib Markers) - https://www.w3schools.com/python/matplotlib_markers.asp

[5] Numpy.org (Numpy.array) - https://numpy.org/doc/stable/reference/generated/numpy.array.html

<br/>

__________________________________________________________________________________________________________________________________________________________
