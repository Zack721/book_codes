# NullPointer should be set to -1 if using array element with index 0


# Declare record type to store data and pointer

class Node:
    def __init__(self):
        self.Data = None
        self.Pointer = -1
        
class Queue:
    def __init__(q, max_capacity):
        q.queue_ = [Node() for i in range(max_capacity)]
        q.size_ = 0
        q.max_ = max_capacity
        q.front_ = -1 
        q.end_ = -1 
       
        
        #FreeListPtr = 0 

    def JoinQueue(q, NewItem):
        if q.size_ < q.max_:
            if q.size_ == 0:
                q.front_ = 0

            q.end_ += 1
            q.size_ += 1
            
            if q.end_ > q.max_:
                q.end_ = 0

            
            q.queue_[q.end_].Data = NewItem
            q.queue_[q.end_].Pointer = -1

        else:
            print("No space for more data")
        
    def LeaveQueue(q):
        if q.size_ != 0:  # not an empty queue
            print("Queue empty")
        else:
            q.queue_[q.front_].Data = None
            q.queue_[q.front_].Pointer = -1
            
            q.size_ -= 1
            q.front_ += 1
            
            
        

    def OutputAllNodes(q):
        CurrentNodePtr = q.queue_[q.front_-1].Pointer  # start at beginning of queue
        if q.size_ == 0:
            print("No data in queue")
        else:
            for i in range(q.size_):# was gonna keep while loop but wouldnt print anything
                if i == 0:
                    print("[") 

                print(q.queue_[i].Data)

                if i == q.size_ - 1:
                    print("]")





"""def GetOption():
    print("1: join queue")
    print("2: leave queue")
    print("3: output queue")
    print("4: end program")
    option = input("Enter your choice: ")
    return option
"""



# Main program
"""Queue, HeadOfQueue, EndOfQueue, FreeListPtr = InitialiseQueue()
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
"""


if __name__ == "__main__":
    queue = Queue(8)

    for i in range(8):
        queue.JoinQueue(i)

    

    queue.OutputAllNodes()



