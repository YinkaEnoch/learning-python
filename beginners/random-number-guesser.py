'''
Guess the Number Game Python Project
'''

import random

counter = 0;

while(True):
    print('Counter: ', counter, "\n")
    userInput = int(input("Enter a number: "))
    randomNumber = int(random.random() * 10)
    print(randomNumber)

    if(randomNumber == userInput):
        print('Yea')
        break;
    else:
        print('Try again...')
        counter += 1
