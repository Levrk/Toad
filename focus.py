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
        playsound("files/good.wav")
        sys.exit()
    
    
    def timerStopped():
        #timerStopped is triggered when the script does not register any mouse movement for 5 consecutive minutes
        playsound("files/bad.mp3")
        
    # Timer function
    def timer():
        global mouse_moved
        mouse_moved = False
        print(endTime , " minute timer started.")
        # Wait for 10 seconds (you can adjust the duration) ###needs work change to five minutes
        for _ in range(10):
            if (time.time() >= (startTime + endTime)):
                timerComplete()
            if mouse_moved: 
                return
            threading.Event().wait(1)
        timerStopped()

    # Create a listener for mouse events
    with Listener(on_move=on_move) as listener:
        print("Mouse tracking started. Press Ctrl+C to exit.")
        while True:
            timer()