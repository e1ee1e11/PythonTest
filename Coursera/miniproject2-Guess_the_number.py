"""
This program only can be runned on CodeSkulptor because of its simplegui module
http://www.codeskulptor.org/#user39_OawbAET1Rdp0Xpl.py
"""

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

secret_number = 0
guess_count = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
 

    # remove this when you add your code    
    range100()


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code    
    global secret_number 
    global guess_count
    
    secret_number = random.randrange(0, 100)
    guess_count = 7
    
    print "New game. Range is from 0  to 100."
    print "Number of remaining guesses is", guess_count
    print ""
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number 
    global guess_count
    
    secret_number = random.randrange(0, 1000)
    guess_count = 10
    
    print "New game. Range is from 0  to 1000."
    print "Number of remaining guesses is", guess_count
    print ""
    
def input_guess(guess):
    # main game logic goes here
    global secret_number
    global guess_count

    guess = int(guess)
    print "Guess was", guess
    if guess > secret_number:
        guess_count -= 1
        print "Number of remaining guesses is", guess_count
        print "Lower"
        print ""
    elif guess < secret_number:
        guess_count -= 1
        print "Number of remaining guesses is", guess_count
        print "Higher"
        print ""
    elif guess == secret_number:
        print "Correct"   
        print ""
        new_game()
    else:
        print "something error!"
    # remove this when you add your code
    
    if guess_count <= 0:
        new_game()    
    
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)
# register event handlers for control elements and start frame
button_range100 = frame.add_button("Range: 0 - 100", range100,120)
button_range1000 = frame.add_button("Range: 0 - 1000", range1000,120)
inp = frame.add_input('Guess the number', input_guess, 110)
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
