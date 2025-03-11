# NullPointer should be set to -1 if using array element with index 0
NULLPOINTER = -1

# Declare record type to store data and pointer
class Node:
    def __init__(self):
        self.data = None
        self.pointer = NULLPOINTER

class LinkedList:
    def __init__(self, max_capacity):
        self.list_ = [Node() for i in range(max_capacity)]
        self.pointer_to_smallest_node = NULLPOINTER  # set start pointer
        self.FreeListPtr = 0  # set starting position of free self.nodes_
        for i in range(max_capacity - 1):  # link all nodes to make free self.nodes_
            self.list_[i].pointer = i + 1
        self.list_[max_capacity - 1].pointer = NULLPOINTER  # last node of free self.nodes_
        #return (self.nodes_, self.start_pointer_, self.free_index_)

    def InsertNode(self, new_item):
        if self.FreeListPtr != NULLPOINTER:
            # there is space in the array
            # take node from free self.nodes_ and store data item
            new_items_index = self.FreeListPtr
            self.list_[new_items_index].data = new_item
            self.FreeListPtr = self.list_[self.FreeListPtr].pointer

            # find insertion point
            previous_node_ptr = NULLPOINTER 
        
            current_node_pointer = self.pointer_to_smallest_node  # start at beginning of self.list_
            while current_node_pointer != NULLPOINTER and self.list_[current_node_pointer].data < new_item:
                # while not end of self.list_
                previous_node_ptr = current_node_pointer  # remember this node
                # follow the pointer to the next node
                current_node_pointer = self.list_[current_node_pointer].pointer 

            if previous_node_ptr == NULLPOINTER:
                # insert new node at start of self.nodes_
                self.list_[new_items_index].pointer = self.pointer_to_smallest_node 
                self.pointer_to_smallest_node = new_items_index
            else:
                # insert new node between previous node and this node
                self.list_[new_items_index].pointer = self.list_[previous_node_ptr].pointer
                self.list_[previous_node_ptr].pointer = new_items_index
        else:
            print("no space for more data")


    def FindNode(self, item_data):
        # returns pointer to node
        current_node_pointer = self.pointer_to_smallest_node  # start at beginning of self.nodes_
        while current_node_pointer != NULLPOINTER and self.list_[current_node_pointer].data != item_data:
            # not end of self.nodes_, item not found
            # follow the pointer to the next node
            current_node_pointer = self.list_[current_node_pointer].pointer
        return current_node_pointer


    def DeleteNode(self, item_data):
        current_node_pointer = self.pointer_to_smallest_node # start at beginning of self.nodes_
        while current_node_pointer != NULLPOINTER and self.list_[current_node_pointer].data != item_data:
            # while not end of self.nodes_ and item not found
            previous_node_ptr = current_node_pointer  # remember this node
            # follow the pointer to the next node
            current_node_pointer = self.list_[current_node_pointer].pointer

        if current_node_pointer != NULLPOINTER:  # node exists in self.nodes_
            if current_node_pointer == self.pointer_to_smallest_node:  # first node to be deleted
                self.pointer_to_smallest_node = self.list_[self.pointer_to_smallest_node].pointer
            else:
                self.list_[previous_node_ptr].pointer = self.list_[current_node_pointer].pointer
                
            self.list_[current_node_pointer].pointer = self.FreeListPtr
            self.FreeListPtr = current_node_pointer
        else:
            print("data does not exist in the list")

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    container = LinkedList(4)
    container.InsertNode("D")
    container.InsertNode("A")
    container.InsertNode("C")
    container.InsertNode("B")
    for node in container.list_:
        print(node.data, node.pointer)
    print("Success!")


"""def OutputAllNodes(self.nodes_, self.start_pointer_):
    CurrentNodePtr = self.start_pointer_  # start at beginning of self.nodes_
    if self.start_pointer_ == NULLPOINTER:
        print("No data in self.nodes_")
    while CurrentNodePtr != NULLPOINTER:  # while not end of self.nodes_
        print(CurrentNodePtr, " ", self.nodes_[CurrentNodePtr].Data)
        # follow the pointer to the next node
        CurrentNodePtr = self.nodes_[CurrentNodePtr].Pointer

def GetOption():
    print("1: insert a value")
    print("2: delete a value")
    print("3: find a value")
    print("4: output self.nodes_")
    print("5: end program")
    response = input("Enter your choice: ")
    return response

# Main program
self.nodes_, self.start_pointer_, self.free_index_ = Initialiseself.nodes_()
Option = GetOption()

while Option != "5":
    if Option == "1":
        Data = input("Enter the value: ")
        self.nodes_, self.start_pointer_, self.free_index_ = InsertNode(self.nodes_, self.start_pointer_, self.free_index_, Data)
        OutputAllNodes(self.nodes_, self.start_pointer_)
    elif Option == "2":
        Data = input("Enter the value: ")
        self.nodes_, self.start_pointer_, self.free_index_ = DeleteNode(self.nodes_, self.start_pointer_, self.free_index_, Data)
        OutputAllNodes(self.nodes_, self.start_pointer_)
    elif Option == "3":
        Data = input("Enter the value: ")
        CurrentNodePtr = FindNode(self.nodes_, self.start_pointer_, Data)
        if CurrentNodePtr == NULLPOINTER:
            print("data not found")
        print(self.start_pointer_, self.free_index_)
        for i in range(8):
            print(i, " ", self.nodes_[i].Data, " ", self.nodes_[i].Pointer)
    elif Option == "4":
        OutputAllNodes(self.nodes_, self.start_pointer_)
    Option = GetOption()"""

