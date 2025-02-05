NULLPOINTER = -1

# Declare record type to store data and pointer
class TreeNode:
    def __init__(self):
        self.Data = None
        self.LeftPointer = NULLPOINTER
        self.RightPointer = NULLPOINTER

class BinaryTree:
    def __init__(self, max_capacity):
        self.binarytree = [TreeNode() for i in range(max_capacity)]
        self.root_ptr = NULLPOINTER  # Set root pointer
        self.free_ptr = 0  # Set starting position of free list
        for Index in range(7):  # Link all nodes to make free list
            self.binarytree[Index].LeftPointer = Index + 1
        self.binarytree[7].LeftPointer = NULLPOINTER  # Last node points to NULL
        

    def InsertNode(self, NewItem):
        if self.free_ptr != NULLPOINTER:
            # Take node from free list and store data item
            NewNodePtr = self.free_ptr
            self.binarytree [NewNodePtr].Data = NewItem
            self.free_ptr = self.binarytree [self.free_ptr].LeftPointer
            self.binarytree [NewNodePtr].LeftPointer = NULLPOINTER
            self.binarytree [NewNodePtr].RightPointer = NULLPOINTER

            # Check if empty tree
            if self.root_ptr == NULLPOINTER:
                # Insert new node at root
                self.root_ptr = NewNodePtr
            else:
                # Find insertion point
                ThisNodePtr = self.root_ptr
                while ThisNodePtr != NULLPOINTER:
                    PreviousNodePtr = ThisNodePtr  # Remember this node
                    if self.binarytree [ThisNodePtr].Data > NewItem:
                        TurnedLeft = True  # Follow left pointer
                        ThisNodePtr = self.binarytree [ThisNodePtr].LeftPointer
                    else:
                        TurnedLeft = False  # Follow right pointer
                        ThisNodePtr = self.binarytree [ThisNodePtr].RightPointer

                if TurnedLeft:
                    self.binarytree [PreviousNodePtr].LeftPointer = NewNodePtr
                else:
                    self.binarytree [PreviousNodePtr].RightPointer = NewNodePtr
        else:
            print("No space for more data")

    def FindNode(self, SearchItem):
        ThisNodePtr = self.root_ptr  # Start at the root of the tree
        while ThisNodePtr != NULLPOINTER and self.binarytree[ThisNodePtr].Data != SearchItem:
            # While there is a pointer to follow and search item not found
            if self.binarytree[ThisNodePtr].Data > SearchItem:
                ThisNodePtr = self.binarytree[ThisNodePtr].LeftPointer  # Follow left pointer
            else:
                ThisNodePtr = self.binarytree[ThisNodePtr].RightPointer  # Follow right pointer


    def TraverseTree(self, binarytree, root_ptr):
        if self.root_ptr != NULLPOINTER:
            left = TraverseTree(self.binarytree, self.binarytree[self.root_ptr].LeftPointer)
            print(self.binarytree[self.root_ptr].Data)
            right = TraverseTree(self.binarytree, self.binarytree[self.root_ptr].RightPointer)
            print(left)
            print(right)


    
    # Display the current tree structure and free pointer after each operation
    print("\nTree structure:")
    for i in range(8):
        print(f"{i}: Left -> {self.binarytree [i].LeftPointer}, Data -> '{self.binarytree [i].Data}', Right -> {self.binarytree [i].RightPointer}")
    print(f"RootPointer: {self.root_ptr}, FreePtr: {FreePtr}\n")
    

