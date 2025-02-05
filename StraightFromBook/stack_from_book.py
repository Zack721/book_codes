NULLPOINTER = -1
class Stack:
    def __init__(self, max_capacity):
        self.max_ = max_capacity
        self.base_of_stack_ptr = 0
        self.top_of_stack_ptr = NULLPOINTER
        self.stack_ = [None for i in range(self.max_)]


    def Push(self, NewItem):
        if self.top_of_stack_ptr < self.max_ - 1:
            self.top_of_stack_ptr += 1
            self.stack_[self.top_of_stack_ptr] = NewItem
        else:
            print("Stack full")
        

    """(original didnt like)def Pop(self, Item):
        if self.top_of_stack_ptr == NULLPOINTER:
            print("No data on stack")
        else:
            Item = self.stack_[self.top_of_stack_ptr]
            self.top_of_stack_ptr -= 1   
    """

    def Pop(self):
        if self.top_of_stack_ptr != NULLPOINTER:
            self.top_of_stack_ptr -=1
        
        else:
            print("No data on stack")

    def OutputStack(self):
        CurrentNodePtr = self.top_of_stack_ptr  # start at top of stack
        if self.top_of_stack_ptr == NULLPOINTER:
            print("No data on stack")
        else:
            while CurrentNodePtr >= self.base_of_stack_ptr:  # while not at base of stack
                print(CurrentNodePtr, " ", self.stack_[CurrentNodePtr])
                CurrentNodePtr -= 1


if __name__ == "__main__":
    stack_ = Stack(8)
    stack_.Push(12)
    stack_.Push(11)
    stack_.Push(13)
    stack_.Push(14)
    stack_.Push(111)
    stack_.Push(9)
    stack_.OutputStack()
    stack_.Pop()
    print("\n")
    stack_.OutputStack()
    
