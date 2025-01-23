# NullPointer should be set to -1 if using array element with index 0
EMPTYSTRING = ""
NULLPOINTER = -1
MAXSTACKSIZE = 8
BASEOFSTACKPOINTER = 0

def InitialiseStack():
    TopOfStackPointer = NULLPOINTER
    Stack = [EMPTYSTRING for i in range(MAXSTACKSIZE)]
    return Stack, TopOfStackPointer

def Push(Stack, TopOfStackPointer, NewItem):
    if TopOfStackPointer < MAXSTACKSIZE - 1:
        # there is space in the array
        # increment top of stack pointer
        TopOfStackPointer += 1
        # add item to top of stack
        Stack[TopOfStackPointer] = NewItem
    else:
        print("Stack full")
    return Stack, TopOfStackPointer

def Pop(Stack, TopOfStackPointer):
    Item = EMPTYSTRING
    if TopOfStackPointer == NULLPOINTER:
        print("No data on stack")
    else:
        Item = Stack[TopOfStackPointer]
        TopOfStackPointer -= 1
    return Stack, TopOfStackPointer, Item

def OutputStack(Stack, TopOfStackPointer):
    CurrentNodePtr = TopOfStackPointer  # start at top of stack
    if TopOfStackPointer == NULLPOINTER:
        print("No data on stack")
    else:
        while CurrentNodePtr >= BASEOFSTACKPOINTER:  # while not at base of stack
            print(CurrentNodePtr, " ", Stack[CurrentNodePtr])
            CurrentNodePtr -= 1

def GetOption():
    print("1: push a value")
    print("2: pop a value")
    print("3: output stack")
    print("4: end program")
    response = input("Enter your choice: ")
    return response

# Main program
Stack, TopOfStackPointer = InitialiseStack()
Option = GetOption()

while Option != "4":
    if Option == "1":
        Data = input("Enter the value: ")
        Stack, TopOfStackPointer = Push(Stack, TopOfStackPointer, Data)
        OutputStack(Stack, TopOfStackPointer)
    elif Option == "2":
        Stack, TopOfStackPointer, Item = Pop(Stack, TopOfStackPointer)
        print("Data popped: ", Item)
        OutputStack(Stack, TopOfStackPointer)
    elif Option == "3":
        OutputStack(Stack, TopOfStackPointer)
    Option = GetOption()
