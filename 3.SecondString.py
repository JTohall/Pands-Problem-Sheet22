# Programme will ask the user to input a string and outputs every second letter in reverse order
# Author: Jamie Tohall

Sentence = input("Please enter a sentence:")
# Will ask the user to input a sentence, define the sentence as 'Sentence'.

print(Sentence[::-2])
# Using the slicing syntax [::-2] the sentence will be reversed and every second letter will be printed. 
# If I were to do [::-1] the whole sentence will be printed in reverse order without missing words.