#change to minutes 
from pynput.mouse import Listener
import threading
import time
import sys

def main(input):
    # Global variable to track mouse movement
    cont=True
    endTime = int(input)
    startTime = time.time()
    # Function to be called when the mouse is moved
    def on_move(x, y):
        global mouse_moved
        mouse_moved = True

    def timerComplete():
        print("ohhhh yeah!")
        listener.stop()
        sys.exit()
        

    def timerStopped():
        print("you have moved the mouse")
        return

    # Timer function
    def timer():
        global mouse_moved
        mouse_moved = False
        print(endTime , " minute timer started.")
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
        print("Mouse tracking started. Press Ctrl+C to exit.")
        while True:
            timer()

