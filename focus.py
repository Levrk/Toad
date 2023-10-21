#change to minutes 
from pynput.mouse import Listener
import threading
import time
from datetime import datetime
import sys




def main(input):
    # Global variable to track mouse movement
    startTime = time.time()
    endTime = int(input)
    # Function to be called when the mouse is moved
    def on_move(x, y):
        global mouse_moved
        mouse_moved = True

    def timerComplete():
        print("ohhhh yeah!")
        listener.stop()
        sys.exit()
    
    def Integer_to_minutes(seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"

    def getTime():
            timeLeft = int(input) - ((time.time() - startTime))
            return Integer_to_minutes(int(timeLeft))
    
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
