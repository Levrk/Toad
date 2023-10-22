from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt, QTimer
import threading
import time
import focus
import todo


#declaring global variable to be updated by timerUpdate
globalClock = None
globalStartTime = None
globalClockUpdater = QTimer()
globalInput = 30


class MyWindow(QWidget):
    
    def __init__(self):
        #initialize window
        super().__init__()
        layout = QVBoxLayout()
        timer = self.initTimer()
        layout.addLayout(timer)
        todo = self.initTodo()
        layout.addLayout(todo)
        self.setLayout(layout)
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Toad')
        self.show()

    def initTimer(self):
        #initialize timer section
        global globalClock
        # Create a vertical layout to hold the timer section
        layout = QVBoxLayout()
        focusClock = QHBoxLayout()
        
        
        # Create a timer label
        time = QLabel("30")
        time.setAlignment(Qt.AlignCenter)

        # Create a focus/clock 
        focus = QPushButton("Focus")
        focus.clicked.connect(lambda: self.focus(time.text()))

        clock = QLabel("00:00")
        clock.setFixedSize(100,50)
        globalClock = clock

        focusClock.addWidget(focus)
        focusClock.addWidget(clock)

        # Create a horizontal layout to hold the label and buttons
        timerControl = QHBoxLayout()

        # Create buttons on either side of the label
        down = QPushButton("←")
        up = QPushButton("→")

        #connect buttons to functions
        up.clicked.connect(lambda: self.changeTime(True,time.text(),time))
        down.clicked.connect(lambda: self.changeTime(False,time.text(),time))

        # Add buttons and label to the horizontal layout
        timerControl.addWidget(down)
        timerControl.addWidget(time)
        timerControl.addWidget(up)

        #Add sub layouts to main layout
        layout.addLayout(focusClock)
        layout.addLayout(timerControl)

        return layout

    def initTodo(self):
        layout = QVBoxLayout()
        todoLabel = QLabel("To Do:")
        todoLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(todoLabel)
        items = todo.toList()

        #set up item 1
        todo1 = QHBoxLayout()
        todo1del = QPushButton("x")
        todo1Label = QLabel(items[0])
        todo1pro = QPushButton("↑")
        todo1dem = QPushButton("↓")
        todo1.addWidget(todo1del)
        todo1.addWidget(todo1Label)
        todo1.addWidget(todo1pro)
        todo1.addWidget(todo1dem)

        #assign functions
        todo1del.clicked.connect(lambda: self.delete(1,todoLabel))
        todo1dem.clicked.connect(lambda: self.demote(1,todoLabel))
        todo1pro.clicked.connect(lambda: self.promote(1,todoLabel))

        #set up item 2
        todo2 = QHBoxLayout()
        todo2del = QPushButton("x")
        todo2Label = QLabel(items[1])
        todo2pro = QPushButton("↑")
        todo2dem = QPushButton("↓")
        todo2.addWidget(todo2del)
        todo2.addWidget(todo2Label)
        todo2.addWidget(todo2pro)
        todo2.addWidget(todo2dem)

        #assign functions
        todo2del.clicked.connect(lambda: self.delete(2,todoLabel))
        todo2dem.clicked.connect(lambda: self.demote(2,todoLabel))
        todo2pro.clicked.connect(lambda: self.promote(2,todoLabel))

        #set up item 3
        todo3 = QHBoxLayout()
        todo3del = QPushButton("x")
        todo3Label = QLabel(items[2])
        todo3pro = QPushButton("↑")
        todo3dem = QPushButton("↓")
        todo3.addWidget(todo3del)
        todo3.addWidget(todo3Label)
        todo3.addWidget(todo3pro)
        todo3.addWidget(todo3dem)

        #assign functions
        todo3del.clicked.connect(lambda: self.delete(3,todoLabel))
        todo3dem.clicked.connect(lambda: self.demote(3,todoLabel))
        todo3pro.clicked.connect(lambda: self.promote(3,todoLabel))

        #set up item 4
        todo4 = QHBoxLayout()
        todo4del = QPushButton("x")
        todo4Label = QLabel(items[3])
        todo4pro = QPushButton("↑")
        todo4dem = QPushButton("↓")
        todo4.addWidget(todo4del)
        todo4.addWidget(todo4Label)
        todo4.addWidget(todo4pro)
        todo4.addWidget(todo4dem)

        #assign functions
        todo4del.clicked.connect(lambda: self.delete(4,todoLabel))
        todo4dem.clicked.connect(lambda: self.demote(4,todoLabel))
        todo4pro.clicked.connect(lambda: self.promote(4,todoLabel))


        #set up item 5
        todo5 = QHBoxLayout()
        todo5del = QPushButton("x")
        todo5Label = QLabel(items[4])
        todo5pro = QPushButton("↑")
        todo5dem = QPushButton("↓")
        todo5.addWidget(todo5del)
        todo5.addWidget(todo5Label)
        todo5.addWidget(todo5pro)
        todo5.addWidget(todo5dem)

        #assign functions
        todo5del.clicked.connect(lambda: self.delete(5,todoLabel))
        todo5dem.clicked.connect(lambda: self.demote(5,todoLabel))
        todo5pro.clicked.connect(lambda: self.promote(5,todoLabel))

        widgets = [todo1,todo2,todo3,todo4,todo5]

        count = 0
        for item, widget in zip(items,widgets):
            if item == "":
                continue
            else:
                count+=1
                layout.addLayout(widget)
        #add item button only if list is not full
        if count < 5 :
            add = QHBoxLayout()
            textEntry = QLineEdit()
            textEntry.setPlaceholderText("Add Item")
            addButton = QPushButton("+")
            addButton.clicked.connect(lambda: self.add(textEntry.text(),todoLabel))
            add.addWidget(textEntry)
            add.addWidget(addButton)
            layout.addLayout(add)
        return layout
    
    def focus(self, input):
        #focus function initializes the timer and begins updating the clock
        global globalStartTime, globalClockUpdater
        globalStartTime = time.time()
        globalClockUpdater.start(1000)
        timer_process = threading.Thread(target=focus.main, args=(input,))
        timer_process.start()
        return

    def changeTime(self, direction,current,obj):
        #changes timer duration
        global globalInput
        times = ["15","30","45","60","90"]
        index = times.index(current)
        if (direction and index !=4):
            obj.setText(times[index+1])
            globalInput = int(times[index+1])
        elif(not direction and index != 0):
            obj.setText(times[index-1])
            globalInput = int(times[index-1])
        return

    def resetTodo(self, stopPoint):
        #resets todo list section of the UI after making changes to the list
        def find_all_widgets(layout):
            #identify all widgets recursively to be removed and re-added
            widgets = []

            for i in range(layout.count()):
                item = layout.itemAt(i)
                widget = item.widget()
                sub_layout = item.layout()

                if widget:
                    widgets.append(widget)
                if sub_layout:
                    widgets.extend(find_all_widgets(sub_layout))

            return widgets

        layout = self.layout()
        widgets = find_all_widgets(layout)
        index = widgets.index(stopPoint)
        widgets = widgets[index:]
        for widget in widgets:
            layout.removeWidget(widget)

        # Delete the removed widgets to free memory
        for widget in widgets:
            widget.deleteLater()

        #remake the todo section of the GUI
        todo = self.initTodo()
        layout.addLayout(todo)
        


    def add(self,item,stopPoint):
        #add item to the list
        todo.add(item)
        self.resetTodo(stopPoint)
        self.repaint()
        return
    
    def delete(self, item,stopPoint):
        #delete item from the list
        todo.delete(item)
        self.resetTodo(stopPoint)
        self.repaint()
        return
    
    def promote(self, item,stopPoint):
        #promote item to the top of the list
        todo.promote(item)
        self.resetTodo(stopPoint)
        self.repaint()
        return
    
    def demote(self, item,stopPoint):
        #demote item to the bottom of the list
        todo.demote(item)
        self.resetTodo(stopPoint)
        self.repaint()
        return
    
    def updateTime(self):
        #updates clock 
        global globalClock, globalInput
        globalClock.setText(self.getTime(globalStartTime,globalInput))

    
    def Integer_to_minutes(self, seconds):
        #converts integers to minutes:seconds format
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"

    def getTime(self, inputTime,startTime):
        #gets remaining time
        global globalClockUpdater
        timeLeft = int(inputTime) - ((time.time() - startTime))
        if timeLeft <= 0:
            globalClockUpdater.stop()
        else:
            return str(self.Integer_to_minutes(int(timeLeft)))
        


def main():
    app = QApplication([])
    window = MyWindow()
    globalClockUpdater.timeout.connect(window.updateTime)
    window.show()
    app.exec()

main() 