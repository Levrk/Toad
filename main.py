from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt
import focus
import todo

class MyWindow(QWidget):
    
    def __init__(self):
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
        # Create a vertical layout to hold the timer section
        layout = QVBoxLayout()

        
        # Create a timer label
        time = QLabel("25")
        time.setAlignment(Qt.AlignCenter)

        # Create a focus button
        focus = QPushButton("Focus")
        focus.clicked.connect(lambda: self.focus(time))

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

        # Add the button and the horizontal layout to the vertical layout
        layout.addWidget(focus)

        #Add todo list label
        
        
        layout.addLayout(timerControl)

        return layout

    def initTodo(self):
        layout = QVBoxLayout()
        todoLabel = QLabel("To Do:")
        todoLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(todoLabel)
        items = todo.toList()
        print(items)
        todo1 = QHBoxLayout()
        todo1del = QPushButton("x")
        todo1Label = QLabel(items[0])
        todo1pro = QPushButton("↑")
        todo1dem = QPushButton("↓")
        todo1.addWidget(todo1del)
        todo1.addWidget(todo1Label)
        todo1.addWidget(todo1pro)
        todo1.addWidget(todo1dem)

        todo2 = QHBoxLayout()
        todo2del = QPushButton("x")
        todo2Label = QLabel(items[1])
        todo2pro = QPushButton("↑")
        todo2dem = QPushButton("↓")
        todo2.addWidget(todo2del)
        todo2.addWidget(todo2Label)
        todo2.addWidget(todo2pro)
        todo2.addWidget(todo2dem)

        todo3 = QHBoxLayout()
        todo3del = QPushButton("x")
        todo3Label = QLabel(items[2])
        todo3pro = QPushButton("↑")
        todo3dem = QPushButton("↓")
        todo3.addWidget(todo3del)
        todo3.addWidget(todo3Label)
        todo3.addWidget(todo3pro)
        todo3.addWidget(todo3dem)

        todo4 = QHBoxLayout()
        todo4del = QPushButton("x")
        todo4Label = QLabel(items[3])
        todo4pro = QPushButton("↑")
        todo4dem = QPushButton("↓")
        todo4.addWidget(todo4del)
        todo4.addWidget(todo4Label)
        todo4.addWidget(todo4pro)
        todo4.addWidget(todo4dem)


        todo5 = QHBoxLayout()
        todo5del = QPushButton("x")
        todo5Label = QLabel(items[4])
        todo5pro = QPushButton("↑")
        todo5dem = QPushButton("↓")
        todo5.addWidget(todo5del)
        todo5.addWidget(todo5Label)
        todo5.addWidget(todo5pro)
        todo5.addWidget(todo5dem)

        widgets = [todo1,todo2,todo3,todo4,todo5]

        count = 0
        for item, widget in zip(items,widgets):
            if item == "":
                continue
            else:
                count+=1
                layout.addLayout(widget)
        #add item button only if list is not full
        print(count)
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
    
    def focus(self, time):
        print("Focusing for ", time.text())
        return

    def changeTime(self, direction,current,obj):
        #Direction is a bool and True = up and False = down
        times = ["15","25","45","Endless"]
        index = times.index(current)
        if (direction and index !=3):
            obj.setText(times[index+1])
        elif(not direction and index != 0):
            obj.setText(times[index-1])
        return

    def resetTodo(self, stopPoint):
        
        def find_all_widgets(layout):
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

        todo = self.initTodo()
        layout.addLayout(todo)
        


    def add(self,item,stopPoint):
        todo.add(item)
        self.resetTodo(stopPoint)
        self.repaint()
        return
    
def main():
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()

main()