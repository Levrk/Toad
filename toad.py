import sys
import focus
import todo


# parse arguments
try:
    arg1 = sys.argv[1]
except:
    print("No argument provided")
    sys.exit()
try:
    arg2 = sys.argv[2]
except:
    if (arg1 == "focus"):
        print("Missing argument")
        sys.exit()
    else:
        pass


if (arg1 == "focus"):
    focus.main(arg2)
elif (arg1 == "todo"):
    todo.todo()