# NullPointer should be set to -1 if using an array
NULLPOINTER = -1

# Declare record type to store data and pointer
class Node:
    def __init__(self):
        self.data = None
        self.left_pointer = NULLPOINTER
        self.right_pointer = NULLPOINTER

class BinaryTree:
    def __init__(self, capacity):
        self.tree = [Node() for i in range(capacity)]
        self.root_pointer = NULLPOINTER  # set Root pointer
        self.free_ptr = 0  # set starting position of free list
        self.size_ = 0

        # link all nodes to make free list
        for i in range(capacity-1):
            self.tree[i].left_pointer = i + 1

        

    def InsertNode(self, new_item):
        if self.free_ptr != NULLPOINTER:
            # there is space in the array
            # take node from free list and store data item
            new_node_ptr = self.free_ptr
            self.tree[new_node_ptr].data = new_item
            self.free_ptr = self.tree[self.free_ptr].left_pointer
            self.tree[new_node_ptr].left_pointer = NULLPOINTER
            self.tree[new_node_ptr].right_pointer = NULLPOINTER

            # check if tree is empty
            if self.root_pointer == NULLPOINTER:
                # insert new node at root
                self.root_pointer = new_node_ptr
            else:
                # find insertion point
                this_node_ptr = self.root_pointer
                while this_node_ptr != NULLPOINTER:
                    previous_node_ptr = this_node_ptr  # remember this node
                    if self.tree[this_node_ptr].data > new_item:
                        turned_left = True  # follow left pointer
                        this_node_ptr = self.tree[this_node_ptr].left_pointer
                    else:
                        turned_left = False
                        this_node_ptr = self.tree[this_node_ptr].right_pointer

                # insert the new node
                if turned_left:
                    self.tree[previous_node_ptr].left_pointer = new_node_ptr
                else:
                    self.tree[previous_node_ptr].right_pointer = new_node_ptr
                self.size_+= 1
        else:
            print("No space for more data")

    def DeleteNode(self):
        if self.size_ != 0:
            self.size_ -= 1



    def FindNode(self, search_item):
        this_node_ptr = self.root_pointer # start at the root of the tree
        while this_node_ptr != NULLPOINTER and self.tree[this_node_ptr].data != search_item:
            # while there is a pointer to follow and search item not found
            if self.tree[this_node_ptr].data > search_item:
                this_node_ptr = self.tree[this_node_ptr].left_pointer  # follow left pointer
            else:
                this_node_ptr = self.tree[this_node_ptr].right_pointer  # follow right pointer

        if self.tree[this_node_ptr].data == search_item:
            print(f"Found {search_item}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        else:
            print("Doesnt exist in binary tree bozo")


    """def TraverseTree(self, Tree, RootPointer):
        if RootPointer != NULLPOINTER:
            TraverseTree(Tree, Tree[RootPointer].LeftPointer)
            print(Tree[RootPointer].Data)
            TraverseTree(Tree, Tree[RootPointer].RightPointer)"""

    """def GetOption():
        print("1: add data")
        print("2: find data")
        print("3: traverse tree")
        print("4: end program")
        option = input("Enter your choice: ")
        return option

    # Main program
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
                print("Value found at", ThisNodePtr)
        elif Option == "3":
            TraverseTree(Tree, RootPointer)
        else:
            print("Invalid option")
        
        print(RootPointer, FreePtr)
        for i in range(8):
            print(i, " ", Tree[i].LeftPointer, " ", Tree[i].Data, " ", Tree[i].RightPointer)

        Option = GetOption()
"""

if __name__ == "__main__":
    bt = BinaryTree(8)
    bt.InsertNode("Isaac")
    bt.InsertNode("Josias")
    bt.InsertNode("Nathan")
    bt.InsertNode("Josh")
    bt.InsertNode("Jermaine")
    bt.InsertNode("Joseph")
    bt.InsertNode("Taylor")


    bt.FindNode("Josh")
    bt.FindNode("Taylor")