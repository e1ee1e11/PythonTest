"""
This program can only be runned on CodeSkulptor
http://www.codeskulptor.org/#user39_z4KpImLwtkZ3et3.py
"""

# template for "Stopwatch: The Game"

import simplegui

# define global variables
tenths_of_seconds = 0
attempt_number = 0 
success_number = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    #get mintues
    mintues = t // 600
    #remaining t
    t = t - mintues * 600
    # get seconds
    seconds = t // 10
    #remaining t equals to tenths of seconds
    t = t - seconds * 10
    #change the type of seconds to string
    if seconds <10:
        seconds = "0" + str(seconds)
        
    return str(mintues) + ":" + str(seconds) + "." + str(t)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button_func():
    if not timer.is_running():
        timer.start()
    
def stop_button_func():
    global attempt_number 
    global success_number
    if timer.is_running():
        timer.stop()
        attempt_number += 1
        if tenths_of_seconds % 10 == 0:
            success_number += 1
    
def reset_button_func():
    global tenths_of_seconds
    global attempt_number 
    global success_number
    if timer.is_running():    
        timer.stop()
    tenths_of_seconds = 0 
    attempt_number = 0 
    success_number = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global tenths_of_seconds
    tenths_of_seconds += 1
    #canvas.draw_text(format(tenths_of_seconds), [55, 85], 36, "White")

# define draw handler
def draw_handler(canvas):
    global attempt_number 
    global success_number
    canvas.draw_text(format(tenths_of_seconds), [55, 85], 36, "White")
    canvas.draw_text(str(success_number) + "/" + str(attempt_number) \
                     , [160, 20], 22, "Green")
    
# create frame
frame = simplegui.create_frame('Stop Watch', 200, 150)

# register event handlers
button_start = frame.add_button("Start", start_button_func, 100)
button_stop = frame.add_button("Stop", stop_button_func, 100)
button_reset = frame.add_button("Reset", reset_button_func, 100)
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
