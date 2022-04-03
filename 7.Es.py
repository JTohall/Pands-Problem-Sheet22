# Write a programme that reads in a text file and outputs the number of E's it contains
# Author: Jamie Tohall


import sys
# Import the sys module 


filename = sys.argv[1]
# Sys.argv is a command in python that contains all the command-line arguments passed to the script 
# Sys.argv[1] refers to the second argument in the command line, in this case the second argument 
# is 'MobyDick.txt'

# The command line is formatted like so: 'python 7.Es.py MobyDick.txt'
# The text file also has to be in the same folder as the programme (Pands-Problem-Sheet22)


with open (filename, "rt") as f: 
#"rt" will open the MobyDick.txt file in read and text mode, and saved the file as 'f', 
# meaning that 'f' now represents the text file in this programme
    
        data = f.read()
        e = data.count ("e")
        E = data.count ("E") 
        
# data.count will return the number of elements with the specified value, in this case the 
# value is the letter E in both upper and lower case.
# I assume that the count method does not count both upper and lower case letters together so I 
# counted them both seperately, then I will add them together for the output.
        
print("There are a total of {} letter E's in this file".format(e + E))
# To clarify I used an upper case E in the output sentence, however I'm including all upper
# and lower case E's contained in the text file. I added the amount of upper and lower case
# E's together in the format section '(E + e)' to get the final number of 150.
