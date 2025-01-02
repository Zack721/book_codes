class Queue:
    def __init__(self, max_size):
        self.queue_ = ["" for i in range(max_size)]
        self.front_ = -1
        self.end_ = -1
        self.size_ = 0
        self.MAX_SIZE_ = max_size



# NullPointer should be set to -1 if using array element with index

    def AddToQueue(self, new_item):
        if self.size_ == 0:  # first item?
            self.front_ = 0
        
        if self.size_ < self.MAX_SIZE_:
            self.end_ += 1
            # check for wrap-round
            if self.end_ > self.MAX_SIZE_ - 1:
                self.end_ = 0
            self.queue_[self.end_] = new_item
            # increment counter
            self.size_ += 1
        else:
            print("No space for more data")
        
        
    def RemoveFromQueue(self):
        Item = EMPTYSTRING
        if self.size_  > 0:  # not an empty queue
            Item = self.queue_[self.front_]
            self.size_ -= 1
            # if queue now empty, reset front and end pointers
            if self.size_ == 0:
                self.front_ = NULLPOINTER
                self.end_  = NULLPOINTER
            else:
                # increment front of queue pointer
                self.front_ += 1
                # check for wrap-round
                if self.front_ > self.MAX_SIZE_ - 1:
                    self.front_ = 0
        else:
            print("Queue empty")
        

    def OutputQueue(self):    # in editing process
        CurrentItem = self.front_  # start at beginning of queue
        if self.size_ == 0:
            print("No data in queue")
        else:
            for Count in range(self.size_):
                print(CurrentItem, " ", self.queue_[CurrentItem])
                # move to next item in queue
                CurrentItem += 1
                # check for wrap-round
                if CurrentItem > self.MAX_SIZE_ - 1:
                    CurrentItem = 0

def GetOption():
    print("1: join queue")
    print("2: leave queue")
    print("3: output queue")
    print("4: end program")
    Response = input("Enter your choice: ")
    return Response

"""Queue, FrontOfQueue, EndOfQueue, NumberInQueue = InitialiseQueue()
Response = GetOption()

while Response != "4":
    if Response == "1":
        Data = input("Enter the value: ")
        Queue, FrontOfQueue, EndOfQueue, NumberInQueue = AddToQueue(
            Queue, FrontOfQueue, EndOfQueue, NumberInQueue, Data
        )
        OutputQueue(Queue, FrontOfQueue, NumberInQueue)
    elif Response == "2":
        Queue, FrontOfQueue, EndOfQueue, NumberInQueue, Item = RemoveFromQueue(
            Queue, FrontOfQueue, EndOfQueue, NumberInQueue
        )
        print("Data leaving queue: ", Item)
        OutputQueue(Queue, FrontOfQueue, NumberInQueue)
    elif Response == "3":
        OutputQueue(Queue, FrontOfQueue, NumberInQueue)
        print(FrontOfQueue, EndOfQueue, NumberInQueue)
        for i in range(MAXQUEUESIZE):
            print(i, " ", Queue[i])
    Response = GetOption()"""
