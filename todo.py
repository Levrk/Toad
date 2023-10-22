import csv

def toList():
    #returns a list of 5 elements from the todo list with blanks if there are less than 5
    list = []
    with open("files/todo.csv", 'r', newline='') as file:
        reader = csv.reader(file)
        for _ in range(5):
            try:
                row = next(reader)  # Read the next line from the CSV
                list.append(row[0])
            except StopIteration:
                # If there are fewer than 5 lines, add empty strings
                list.append("")
    return list

def promote(item):
    #promote item to the top of the list
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
    #demote item to the bottom of the list
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