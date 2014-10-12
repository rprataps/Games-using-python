# MiniProject3 : "Stopwatch: The Game"
#Stop the watch on a whole second (1.0, 2.0, 3.0, etc.).

import simplegui
import random

# define global variables
count = 0
flag = False
x = [200,250]
a = [400,50]
successes = 0;attempts = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = t/600
    seconds = (t-minutes*600)/10
    one_tenth_sec = t%10
    if(minutes>10):
        minutes -= 10
    if seconds>9:
        num = str(minutes)+':'+str(seconds)+'.'+str(one_tenth_sec)
    else :
        num = str(minutes)+':0'+str(seconds)+'.'+str(one_tenth_sec)      
    return num

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handle():
    global flag
    timer.start()
    flag = True
      
def stop_handle():
    global count,flag,successes,attempts
    timer.stop()
    if flag == True:
        attempts += 1
        if(count%10==0):
            successes = successes+1
    flag = False
        
def reset_handle():
    global count,flag,successes,attempts
    timer.stop()
    count = 0
    successes = 0
    attempts = 0
    flag = False
    
# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count = count+1  

# define draw handler
def draw(canvas):
    global time,count,successes,attempts
    canvas.draw_text(format(count),x,60,"white")
    score_str = str(successes)+'/'+str(attempts)
    canvas.draw_text("Successes / Attempts",[a[0]-30,10],15,"green")
    canvas.draw_text(score_str,a,40,"green")
    
    "Printing some messages on multiple of 5 attempts"
    if attempts%5==0 and attempts>0:
        canvas.draw_text("Your current score is "+ score_str,[20,100],40,"red")
        if successes==attempts and attempts%5==0:
            canvas.draw_text("Excellent! You are a champ.",[20,150],40,"red")
        elif successes>=(.60*attempts) and (attempts%5==0):
            canvas.draw_text("Good! But you can do better.",[20,150],40,"red")
        elif successes<(.60*attempts) and (attempts%5==0):
            canvas.draw_text("Hard Luck! Need to improve.",[20,150],40,"red")

# creating frame
frame = simplegui.create_frame("StopWatch Game",500,300)

# registering event handlers
timer = simplegui.create_timer(100,tick)
button1 = frame.add_button('START', start_handle,200)
button2 = frame.add_button('STOP', stop_handle,200)
button3 = frame.add_button('RESET', reset_handle,200)
frame.set_draw_handler(draw)

# starting timer and frame
frame.start()

