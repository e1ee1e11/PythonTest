"""
This program only can be runned on CodeSkulptor
http://www.codeskulptor.org/#user39_mep3VhPzAVU1i2Y.py
"""

# implementation of card game - Memory

import simplegui
import random
memory16_list = range(8) + range(8)
#exposed_list = [False for False in range(16)]
CARD_WIDTH = 50
CARD_HEIGHT = 100
turns = 0
# helper function to initialize globals
def new_game():
    global memory16_list, exposed_list, state, turns
    state = 0
    turns = 0
    exposed_list = [False for False in range(16)]
    random.shuffle(memory16_list)
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed_list, memory16_list, idx1, idx2, turns
    if state == 0:
        idx1 = pos[0] // CARD_WIDTH
        exposed_list[idx1] = True
        state = 1
    elif state == 1:
        idx2 = pos[0] // CARD_WIDTH
        if exposed_list[idx2] != True:
            exposed_list[idx2] = True
            state = 2    
            turns += 1
    else:
        idx = pos[0] // CARD_WIDTH
        if exposed_list[idx] != True:
            exposed_list[idx] = True
            state = 1
            if memory16_list[idx1] !=  memory16_list[idx2]:
                exposed_list[idx1] = False 
                exposed_list[idx2] = False
            idx1 = idx   
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global memory16_list, exposed_list
    for idx, num in enumerate(memory16_list):
        if exposed_list[idx] == True:
            canvas.draw_text(str(num), [CARD_WIDTH / 3 + idx * CARD_WIDTH, CARD_HEIGHT / 1.5],\
                         50, 'White')
    for idx, num in enumerate(exposed_list):
        if exposed_list[idx] == False:
            canvas.draw_polygon([[CARD_WIDTH * idx, 0], [CARD_WIDTH* (idx+1), 0],\
                                [CARD_WIDTH * (idx+1), CARD_HEIGHT], [CARD_WIDTH* idx, CARD_HEIGHT]],\
                                4, 'Olive', 'Green')        
    label.set_text('Turns = ' + str(turns))
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label('Turns = ' + str(turns))
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
