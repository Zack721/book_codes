# NullPointer should be set to -1 if using array element with index 0
NULLPOINTER = -1

# Declare record type to store data and pointer
class TreeNode:
    def __init__(self):
        self.Data = ""
        self.LeftPointer = NULLPOINTER
        self.RightPointer = NULLPOINTER

def InitialiseTree():
    Tree = [TreeNode() for i in range(8)]
    RootPointer = NULLPOINTER  # Set root pointer
    FreePtr = 0  # Set starting position of free list
    for Index in range(7):  # Link all nodes to make free list
        Tree[Index].LeftPointer = Index + 1
    Tree[7].LeftPointer = NULLPOINTER  # Last node points to NULL
    return Tree, RootPointer, FreePtr

def InsertNode(Tree, RootPointer, FreePtr, NewItem):
    if FreePtr != NULLPOINTER:
        # There is space in the array
        # Take node from free list and store data item
        NewNodePtr = FreePtr
        Tree[NewNodePtr].Data = NewItem
        FreePtr = Tree[FreePtr].LeftPointer
        Tree[NewNodePtr].LeftPointer = NULLPOINTER
        Tree[NewNodePtr].RightPointer = NULLPOINTER

        # Check if empty tree
        if RootPointer == NULLPOINTER:
            # Insert new node at root
            RootPointer = NewNodePtr
        else:
            # Find insertion point
            ThisNodePtr = RootPointer
            while ThisNodePtr != NULLPOINTER:
                PreviousNodePtr = ThisNodePtr  # Remember this node
                if Tree[ThisNodePtr].Data > NewItem:
                    TurnedLeft = True  # Follow left pointer
                    ThisNodePtr = Tree[ThisNodePtr].LeftPointer
                else:
                    TurnedLeft = False  # Follow right pointer
                    ThisNodePtr = Tree[ThisNodePtr].RightPointer

            if TurnedLeft:
                Tree[PreviousNodePtr].LeftPointer = NewNodePtr
            else:
                Tree[PreviousNodePtr].RightPointer = NewNodePtr
    else:
        print("No space for more data")
    
    return Tree, RootPointer, FreePtr

def FindNode(Tree, RootPointer, SearchItem):
    ThisNodePtr = RootPointer  # Start at the root of the tree
    while ThisNodePtr != NULLPOINTER and Tree[ThisNodePtr].Data != SearchItem:
        # While there is a pointer to follow and search item not found
        if Tree[ThisNodePtr].Data > SearchItem:
            ThisNodePtr = Tree[ThisNodePtr].LeftPointer  # Follow left pointer
        else:
            ThisNodePtr = Tree[ThisNodePtr].RightPointer  # Follow right pointer
    return ThisNodePtr

def TraverseTree(Tree, RootPointer):
    if RootPointer != NULLPOINTER:
        TraverseTree(Tree, Tree[RootPointer].LeftPointer)
        print(Tree[RootPointer].Data)
        TraverseTree(Tree, Tree[RootPointer].RightPointer)

def GetOption():
    print("1: Add data")
    print("2: Find data")
    print("3: Traverse tree")
    print("4: End program")
    option = input("Enter your choice: ")
    return option

# Main Program
Tree, RootPointer, FreePtr = InitialiseTree()
Option = GetOption()

while Option != "4":
    if Option == "1":
        Data = input("Enter the value: ")
        Tree, RootPointer, FreePtr = InsertNode(Tree, RootPointer, FreePtr, Data)
        TraverseTree(Tree, RootPointer)
    elif Option == "2":
        Data = input("Enter search value: ")
        ThisNodePtr = FindNode(Tree, RootPointer, Data)
        if ThisNodePtr == NULLPOINTER:
            print("Value not found")
        else:
            print("Value found at position", ThisNodePtr)
    elif Option == "3":
        TraverseTree(Tree, RootPointer)
    
    # Display the current tree structure and free pointer after each operation
    print("\nTree structure:")
    for i in range(8):
        print(f"{i}: Left -> {Tree[i].LeftPointer}, Data -> '{Tree[i].Data}', Right -> {Tree[i].RightPointer}")
    print(f"RootPointer: {RootPointer}, FreePtr: {FreePtr}\n")
    
    Option = GetOption()
