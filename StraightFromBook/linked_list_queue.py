# NullPointer should be set to -1 if using array element with index 0
NULLPOINTER = -1

# Declare record type to store data and pointer
class Node:
    def __init__(self):
        self.Data = ""
        self.Pointer = NULLPOINTER

def InitialiseQueue():
    Queue = [Node() for i in range(8)]
    HeadOfQueue = NULLPOINTER  # set Head of Queue pointer
    EndOfQueue = NULLPOINTER  # set End of Queue pointer
    FreeListPtr = 0  # set starting position of free list
    for Index in range(7):  # link all nodes to make free list
        Queue[Index].Pointer = Index + 1
    Queue[7].Pointer = NULLPOINTER  # last node of free list
    return Queue, HeadOfQueue, EndOfQueue, FreeListPtr

def JoinQueue(Queue, HeadOfQueue, EndOfQueue, FreeListPtr, NewItem):
    if FreeListPtr != NULLPOINTER:
        # there is space in the array
        # take node from free list and store data item
        NewNodePtr = FreeListPtr
        Queue[NewNodePtr].Data = NewItem
        FreeListPtr = Queue[FreeListPtr].Pointer
        Queue[NewNodePtr].Pointer = NULLPOINTER

        # find insertion point
        if EndOfQueue == NULLPOINTER:
            # insert new node at start of Queue
            HeadOfQueue = NewNodePtr
        else:
            Queue[EndOfQueue].Pointer = NewNodePtr
        EndOfQueue = NewNodePtr
    else:
        print("No space for more data")
    return Queue, HeadOfQueue, EndOfQueue, FreeListPtr

def LeaveQueue(Queue, HeadOfQueue, EndOfQueue, FreeListPtr):
    if HeadOfQueue != NULLPOINTER:  # not an empty queue
        Value = Queue[HeadOfQueue].Data
        ThisNodePtr = Queue[HeadOfQueue].Pointer
        if ThisNodePtr == NULLPOINTER:
            EndOfQueue = NULLPOINTER  # deleted last item in Queue
        Queue[HeadOfQueue].Pointer = FreeListPtr
        FreeListPtr = HeadOfQueue
        HeadOfQueue = ThisNodePtr
    else:
        print("Queue empty")
        Value = ""
    return Queue, HeadOfQueue, EndOfQueue, FreeListPtr, Value

def OutputAllNodes(Queue, HeadOfQueue):
    CurrentNodePtr = HeadOfQueue  # start at beginning of queue
    if HeadOfQueue == NULLPOINTER:
        print("No data in queue")
    else:
        while CurrentNodePtr != NULLPOINTER:  # while not end of queue
            print(CurrentNodePtr, " ", Queue[CurrentNodePtr].Data)
            # follow the pointer to the next node
            CurrentNodePtr = Queue[CurrentNodePtr].Pointer

def GetOption():
    print("1: join queue")
    print("2: leave queue")
    print("3: output queue")
    print("4: end program")
    option = input("Enter your choice: ")
    return option

# Main program
Queue, HeadOfQueue, EndOfQueue, FreeListPtr = InitialiseQueue()
Option = GetOption()

while Option != "4":
    if Option == "1":
        Data = input("Enter the value: ")
        Queue, HeadOfQueue, EndOfQueue, FreeListPtr = JoinQueue(Queue, HeadOfQueue, EndOfQueue, FreeListPtr, Data)
        OutputAllNodes(Queue, HeadOfQueue)
    elif Option == "2":
        Queue, HeadOfQueue, EndOfQueue, FreeListPtr, Value = LeaveQueue(Queue, HeadOfQueue, EndOfQueue, FreeListPtr)
        print("Data leaving queue: ", Value)
        OutputAllNodes(Queue, HeadOfQueue)
    elif Option == "3":
        OutputAllNodes(Queue, HeadOfQueue)
        print(HeadOfQueue, EndOfQueue, FreeListPtr)
        for i in range(8):
            print(i, " ", Queue[i].Data, " ", Queue[i].Pointer)
    Option = GetOption()
