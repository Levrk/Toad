#account for double digit number of items

import csv

def todo():
    count = read()
    print("n^ to promote, n- to demote, n! to delete nth element")
    print("+x to add x to list")
    userInput = input("-> ")
    if (userInput == ""):
        return
    n = int(userInput[0])
    command = userInput[1]
    if (n > count or n < 1):
        print("your list has no element ", n)
    elif (command == '+'):
        promote(userInput[0])
    elif (command == '-'):
        demote(userInput[0])
    elif (command == '!'):
        delete(userInput[0])
    else:
        return

def read():
    with open('todo.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        count = 1
        for row in reader:
            item = row[0].strip()
            print(count , ". " , item, "\n")
            count+=1
        return count-1
        

def promote(item):
    print("promote")
    return

def demote(item):
    print("demote")
    return

def delete(item):
    print("delete")
    return


