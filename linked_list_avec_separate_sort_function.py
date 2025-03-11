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
        self.max_ = max_capacity

        for i in range(max_capacity):
            self.list[i].pointer = i+1

        self.list[max_capacity-1].pointer = NULLPOINTER

    def Size(self):
            return self.size
    
    def InsertNode(self, new_item):
        if self.size != self.max_:
            self.list[self.free_list_ptr].data = new_item
            self.size +=1
            for i in range(self.max_):
                if self.list[i].data == None:
                    self.free_list_ptr = i
                    break

        else:
            print("The list is full dimwit")

#couldnt think of a way to only swap them virtually
    def AscendingSort(self):
        #pointer_setter = -1
        for i in range(self.size):
            for j in range(0, self.size-1):
                if self.list[j].data == None:
                    self.list[j].data = 0

                if self.list[j+1].data == None:
                    self.list[j+1].data = 0

                if self.list[j].data > self.list[j+1].data:
                    temp = self.list[j+1].data
                    self.list[j+1].data= self.list[j].data
                    self.list[j].data  = temp   

            self.list[i].pointer = i+1
        self.list[self.size-1].pointer = -1 #had to manually set the pointer of last node to -1

    def DescendingSort(self):
        for i in range(self.size):
            for j in range(0, self.size-1):
                if self.list[j].data == None:
                    self.list[j].data = 0

                if self.list[j+1].data == None:
                    self.list[j+1].data = 0

                if self.list[j].data < self.list[j+1].data:
                    temp = self.list[j].data
                    self.list[j].data= self.list[j+1].data
                    self.list[j+1].data  = temp   

            self.list[i].pointer = i-1
        self.list[0].pointer = NULLPOINTER


    def Print(self):
        for a in range(self.max_):
            print(self.list[a].data, self.list[a].pointer)

def main():
    ll = LinkedList(8)
    ll.InsertNode(11)
    ll.InsertNode(7)
    ll.InsertNode(2)

    ll.InsertNode(1)
    ll.InsertNode(12)

    ll.DescendingSort()
    ll.Print()
    ll.AscendingSort()
    ll.Print()

main()
