import csv

def todo():
    count = read()
    print("n^ to promote, n- to demote, n! to delete nth element")
    print("+x to add x to list")
    userInput = input("-> ")
    if (userInput == ""):
        return
    if (userInput[0] == '+'):
        #adding element to todo list
        add(userInput[1:])
    else:
        try:
            n = int(userInput[0:-1])
        except:
            print("invalid input")
            return
        command = userInput[-1]
        if (n > count or n < 1):
            #index out of bounds
            print("your list has no element ", n)
        elif (command == '+'):
            #promoting element
            promote(n)
        elif (command == '-'):
            #demoting element
            demote(n)
        elif (command == '!'):
            #deleting element
            delete(n)

def read():
    with open('files/todo.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        count = 1
        for row in reader:
            item = row[0].strip()
            print(count , ". " , item, "\n")
            count+=1
        return count-1
        

def promote(item):
    print("promote ", item)
    return

def demote(item):
    print("demote ", item)
    return

def delete(item):
    print("delete ", item)
    return

def add(item):
    print("add ", item)
    return


