NULLPOINTER = -1

class Stack:
    def __init__(self, max_capacity):
        self.stack_ = [None for i in range(max_capacity)]
        self.top_of_stack_ptr = NULLPOINTER
        self.max_ = max_capacity

    def Push(self, new_item):
        if self.top_of_stack_ptr > self.max_-1:
            print("Stack is full nincompoop")

        else:
            self.top_of_stack_ptr +=1
            self.stack_[self.top_of_stack_ptr] = new_item

    def Pop(self):
        if self.top_of_stack_ptr == NULLPOINTER:
            print("Stack is empty dingus")

        else:
            self.top_of_stack_ptr-=1

if __name__ == "__main__":
    staaaack = Stack(8)
    staaaack.Push(12)
    staaaack.Push(3)
    staaaack.Push(4)
    staaaack.Push(11)
    staaaack.Push(18)
    staaaack.Push(1)
    index = 0
    for i in staaaack.stack_:
        print(i, index)
        index+=1
    print("\n")
    print("\n")
    staaaack.Pop()
    staaaack.Pop()
    staaaack.Pop()
    index = 0
    for i in range(0, staaaack.top_of_stack_ptr +1):
        print(staaaack.stack_[i], index)
        index+=1

    