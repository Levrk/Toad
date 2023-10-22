#change to minutes 
from pynput.mouse import Listener
import threading
import time
import sys
from playsound import playsound


# Create a condition variable for synchronization with timer stopped
condition = threading.Condition()

def main(input):
    # Global variable to track mouse movement
    startTime = time.time()
    endTime = int(input)
    # Function to be called when the mouse is moved
    def on_move(x, y):
        global mouse_moved
        mouse_moved = True
        

    def timerComplete():
        #play good sound on timer completion
        playsound("files/good.mp3")
        sys.exit()
    
    
    def timerStopped():
        #timerStopped is triggered when the script does not register any mouse movement for 5 consecutive minutes
        playsound("files/bad.mp3")
        

    def timer():
        #to be executed repeatedly while focus.py script is active
        global mouse_moved
        mouse_moved = False
        # Wait for 10 seconds (you can adjust the duration)
        for _ in range(10):
            if (time.time() >= (startTime + endTime)):
                timerComplete()
            if mouse_moved: 
                return
            threading.Event().wait(1)
        timerStopped()

    # Create a listener for mouse events
    with Listener(on_move=on_move) as listener:
        while True:
            timer()