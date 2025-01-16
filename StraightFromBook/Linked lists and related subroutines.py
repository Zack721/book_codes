# NullPointer should be set to -1 if using array element with index 0
NULLPOINTER = -1

# Declare record type to store data and pointer
class Node:
    def __init__(self, data = None):
        self.data = data
        self.pointer = NULLPOINTER    

class LinkedList:
    def __init__(LL, max_capacity):
        LL.list_ = [Node() for i in range(max_capacity)]
        LL.__start_ = NULLPOINTER  # set start pointer
        LL.free_list_ptr_ = 0  # set starting position of free list
        LL.__size_ = 0
        LL.__capacity_ = max_capacity

        for Index in range(7):  # link all nodes to make free list
            LL.list_[Index].pointer = Index + 1
        LL.list_[max_capacity - 1].pointer = NULLPOINTER  # last node of free list
        #return (List, StartPointer, FreeListPtr)

    def InsertNode(LL, new_item):#List, StartPointer, FreeListPtr, NewItem
        if LL.free_list_ptr_ != NULLPOINTER:  #is empty?
            current_index = LL.free_list_ptr_   
            LL.list_[current_index].data = new_item
            LL.free_list_ptr_ = LL.list_[LL.free_list_ptr_].pointer
           
            previous_node_ptr = NULLPOINTER
            this_node_ptr = LL.__start_  # start at beginning of list

            while this_node_ptr != NULLPOINTER and LL.list_[this_node_ptr].data < new_item:   #HAS SORTING MECHANISM "and LL.list_[this_node_ptr].data < new_item"
                # while not end of list
                previous_node_ptr = this_node_ptr  # remember this node
                # follow the pointer to the next node
                this_node_ptr = LL.list_[this_node_ptr].pointer

            if previous_node_ptr == NULLPOINTER:
                LL.list_[current_index].pointer = LL.__start_ 
                LL.__start_  = current_index
            else:
                # insert new node between previous node and this node
                LL.list_[current_index].pointer = LL.list_[previous_node_ptr].pointer
                LL.list_[previous_node_ptr].pointer = current_index
        else:
            print("no space for more data")
        #return (List, StartPointer, FreeListPtr)



if __name__ == "__main__":

    obj = LinkedList(8)
    obj.InsertNode("c")
    obj.InsertNode("b")
    obj.InsertNode("a")
    print(obj.free_list_ptr_ )
    

    for i in obj.list_:
        print(i.data, i.pointer)
    


    def FindNode(LL):#List, StartPointer, DataItem
        # returns pointer to node
        CurrentNodePtr = StartPointer  # start at beginning of list
        while CurrentNodePtr != NULLPOINTER and List[CurrentNodePtr].Data != DataItem:
            # not end of list, item not found
            # follow the pointer to the next node
            CurrentNodePtr = List[CurrentNodePtr].Pointer
        #return CurrentNodePtr  # returns NullPointer if item not found

    def DeleteNode(LL):#List, StartPointer, FreeListPtr, DataItem
        ThisNodePtr = StartPointer  # start at beginning of list
        while ThisNodePtr != NULLPOINTER and List[ThisNodePtr].Data != DataItem:
            # while not end of list and item not found
            PreviousNodePtr = ThisNodePtr  # remember this node
            # follow the pointer to the next node
            ThisNodePtr = List[ThisNodePtr].Pointer

        if ThisNodePtr != NULLPOINTER:  # node exists in list
            if ThisNodePtr == StartPointer:  # first node to be deleted
                StartPointer = List[StartPointer].Pointer
            else:
                List[PreviousNodePtr].Pointer = List[ThisNodePtr].Pointer
            List[ThisNodePtr].Pointer = FreeListPtr
            FreeListPtr = ThisNodePtr
        else:
            print("data does not exist in list")

        #return (List, StartPointer, FreeListPtr)  """
"""
def OutputAllNodes(List, StartPointer):
    CurrentNodePtr = StartPointer  # start at beginning of list
    if StartPointer == NULLPOINTER:
        print("No data in list")
    while CurrentNodePtr != NULLPOINTER:  # while not end of list
        print(CurrentNodePtr, " ", List[CurrentNodePtr].Data)
        # follow the pointer to the next node
        CurrentNodePtr = List[CurrentNodePtr].Pointer

def GetOption():
    print("1: insert a value")
    print("2: delete a value")
    print("3: find a value")
    print("4: output list")
    print("5: end program")
    response = input("Enter your choice: ")
    return response

# Main program
List, StartPointer, FreeListPtr = InitialiseList()
Option = GetOption()

while Option != "5":
    if Option == "1":
        Data = input("Enter the value: ")
        List, StartPointer, FreeListPtr = InsertNode(List, StartPointer, FreeListPtr, Data)
        OutputAllNodes(List, StartPointer)
    elif Option == "2":
        Data = input("Enter the value: ")
        List, StartPointer, FreeListPtr = DeleteNode(List, StartPointer, FreeListPtr, Data)
        OutputAllNodes(List, StartPointer)
    elif Option == "3":
        Data = input("Enter the value: ")
        CurrentNodePtr = FindNode(List, StartPointer, Data)
        if CurrentNodePtr == NULLPOINTER:
            print("data not found")
        print(StartPointer, FreeListPtr)
        for i in range(8):
            print(i, " ", List[i].Data, " ", List[i].Pointer)
    elif Option == "4":
        OutputAllNodes(List, StartPointer)
    Option = GetOption()
"""