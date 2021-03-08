import random

#def guess(x):# Our fruntion to generate a random numbe
    #random_number = random.randint(1, x)#random.randint generates a random integer
    #guess=0# An initialization

   # while guess != random_number:#!= means not equal to
        #guess=int(input (f'Guess a number between 1 and {x}:'))
        #if guess < random_number:
            #print(f'Opps! This number {guess} too low.')
        #elif guess > random_number:
            #print(f'Woah! The number {guess} is too high.')

        
   # print(f'Hooray!!! You guessed {random_number} correctly.')

#guess(10) 


def computer_guess(x):
    
    low_set =1
    high_set = x
    feedback = ' '

    while feedback != 'c':
        #This if else loop is used because if high_set and low_set are the same number, random.randint() gives an error value.
        #It allows us to break outside loop if low_set = high_set
        if low_set != high_set: #This ensures that only in the event that the low_set is not equal to the high_set, that's when we use the function
            guess=random.randint(low_set,high_set)
        else:#This means the high_set and low_set are equal and the guess is correct.
            guess = high_set# Could also be low_set as it's = to high
        guess= random.randint(low_set,high_set)# Ensures that the bounds can be changed according to the user's feedback. Instead of having a fixed 1 to x
        feedback=input(f'Is {guess} too low(L), too high(H) or correct(C)').lower()#We're asking user for feedback
        if feedback == 'h':
            high_set = guess - 1 # If the guess is 8 and it's too high this becomes our upper bound & we need to go lower
        elif feedback == 'l':
            low_set = guess + 1 # If the guess is let's say 2 and this value is too low, it becomes our lower bound & we need to move higher
    print(f'Hurray! The computer guessed, {guess} correctly.')

computer_guess(100)
            





