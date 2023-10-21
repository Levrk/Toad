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
        print(userInput[1:])
        add(userInput[1:])
        read()
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
        elif (command == '^'):
            #promoting element
            promote(n)
            read()
        elif (command == '-'):
            #demoting element
            demote(n)
            read()
        elif (command == '!'):
            #deleting element
            delete(n)
            read()

def read():
    print("To Do: \n")
    with open('files/todo.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        count = 1
        for row in reader:
            item = row[0].strip()
            print(count , ". " , item, "\n")
            count+=1
        return count-1
        

def promote(item):
    # Read the CSV file
    with open("files/todo.csv", 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Move the nth line to the top
    line_to_move = data.pop(item - 1)
    data.insert(0, line_to_move)

    # Write the modified data to a new CSV file
    with open("files/todo.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    return

def demote(item):
    # Read the CSV file
    with open("files/todo.csv", 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Move the nth line to the top
    line_to_move = data.pop(item - 1)
    data.append(line_to_move)

    # Write the modified data to a new CSV file
    with open("files/todo.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    return

def delete(item):
    # Read the CSV file
    with open("files/todo.csv", 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # delete the nth line to the top
    data.pop(item - 1)

    # Write the modified data to a new CSV file
    with open("files/todo.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    return

def add(item):
        # Read the CSV file
    with open("files/todo.csv", 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # delete the nth line to the top
    data.insert(0, [item])

    # Write the modified data to a new CSV file
    with open("files/todo.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    return