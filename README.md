# Productivity Toad is a python based To-do list and productivity timer for students struggling with ADHD

## Quick-Start Instructions

The application can be launched from within the main directory using the following command: 

```
python main.py
```

Please ensure you have all of the dependencies installed before running the script. Required dependancies are listed in requirements.txt.

## Inspiration
My inspiration for this project came from my own struggles as a student with ADHD. I wanted to build a simple application which could help students to prioritize and complete a small set of essential tasks. I also am passionate about music production and knew I wanted to work some original music into the project.

## What it does
My program allows students to manage a list of up to 5 essential tasks. It allows them to add or delete items, as well as promoting or demoting them to indicate priority. The program also includes a variable length productivity timer which can help to incentivize focus and monitor activity. This timer monitors user activity through mouse movements and plays an alarm to get their attention if they have been inactive for 5 minutes. 

## How we built it
I built this project entirely in python using a handful of interesting libraries. I used the PyQt5 library to create a GUI so that user's could interact with the application outside of the command line. I used the pynput library to track user input through mouse movements. I used the playsound library to trigger audio files which I composed using Logic Pro. I also used Threading to simultaneously execute scripts from different files without causing the GUI to hang. 

## Challenges we ran into
Most of the challenges I ran into completing this project were related to my initial scope. At a couple moments during this weekend I was forced to re-evaluate my end goal and adjust my project so that it could be completed within the timeframe. I went into this hoping to build this project as a chrome extension, but quickly decided that I would be more successful writing it as a python-based application. 

## Accomplishments that we're proud of
I am very proud of what I was able to accomplish in such a short time. At the beginning of this process I generated a list of features and classified each as "Ideal" or "Essential". Through trials, tribulations, and hours spent fixing bugs I was able to implement all of my "Essential" functions and a few marked as "Ideal". One aspect of the application which I am especially proud of is fact that remaining time is updated live on the GUI. While this may seem like a simple task, executing the timer function from a separate file and reporting data live to the interface while still allowing for use of the application's other features required me to use separate processing threads, which I had never done before. 

## What's next for Productivity Toad
There are a lot of additional features I would like to add to this application. Firstly, I would like to convert the scripts into a single executable file. This would make the application much more accessible to non-programmers. Some other features I would like to include would be custom alarm sounds, a more complex class for todo list items, and comprehensive user input tracking.
