NULLPOINTER = -1

class Node:
    def __init__(self):
        self.data = None
        self.pointer = NULLPOINTER

class LinkedList:
    def __init__(self, max_capacity):
        self.list = [Node() for i in range(max_capacity)]
        self.ptr_to_smallest_node = NULLPOINTER
        self.free_list_ptr = 0
        self.size = 0

        for i in range(max_capacity):
            self.list[i].pointer = i+1

        self.list[max_capacity-1].pointer = NULLPOINTER


    def InsertNode(self, new_item):
        if self.free_list_ptr != NULLPOINTER:
            new_item_index = self.free_list_ptr
            self.list[new_item_index].data = new_item
            self.size +=1
            self.free_list_ptr = self.list[new_item_index].pointer

            previous_node_ptr = NULLPOINTER
            current_node_ptr = self.ptr_to_smallest_node

            while current_node_ptr != NULLPOINTER and self.list[current_node_ptr].data < new_item:
                previous_node_ptr = current_node_ptr

                current_node_ptr = self.list[current_node_ptr].pointer

            if previous_node_ptr == NULLPOINTER:
                self.list[new_item_index].pointer = self.ptr_to_smallest_node
                self.ptr_to_smallest_node = new_item_index
            


            else:
                self.list[new_item_index].pointer = self.list[previous_node_ptr].pointer
                self.list[previous_node_ptr].pointer = new_item_index
            
           
        
        else:
            print("The list is full dimwit")

    def FindNode(self, find_this):
        current_element = self.ptr_to_smallest_node
        while NULLPOINTER != current_element and self.list[current_element].data != find_this:
            current_element = self.list[current_element].pointer
        if self.list[current_element].data == find_this:
            return True
        else:
            return False
            
        

    def DeleteNode(self, item_to_dlt):
        current_node_ptr = self.ptr_to_smallest_node
        while current_node_ptr != NULLPOINTER and self.list[current_node_ptr].data != item_to_dlt:
            previous_node_ptr = current_node_ptr
            current_node_ptr = self.list[current_node_ptr].pointer

        if current_node_ptr != NULLPOINTER:
            self.size -=1
            if current_node_ptr == self.ptr_to_smallest_node:
                self.ptr_to_smallest_node = self.list[self.ptr_to_smallest_node].pointer
            else:
                self.list[previous_node_ptr].pointer = self.list[current_node_ptr].pointer

            self.list[current_node_ptr].pointer = self.free_list_ptr
            self.free_list_ptr = current_node_ptr
        else:
            print("data ins`t in list bozo")

    

    def Size(self):
        return self.size 













if __name__ == "__main__":
    list_thats_linked = LinkedList(8)
    for i in list_thats_linked.list:
        print(i.data, i.pointer)



    list_thats_linked.InsertNode("a")
    list_thats_linked.InsertNode("c")
    list_thats_linked.InsertNode("b")
    list_thats_linked.InsertNode("d")

    print(list_thats_linked.Size())

    for i in list_thats_linked.list:
        print(i.data, i.pointer)

    list_thats_linked.DeleteNode("c")

    print(list_thats_linked.Size())

    for i in list_thats_linked.list:
        print(i.data, i.pointer)

    list_thats_linked.DeleteNode("d")

    for i in list_thats_linked.list:
        print(i.data, i.pointer)


