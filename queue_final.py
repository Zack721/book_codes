class Queue:
    def __init__(self, max_capacity):
        self.__queue_ = [None for i in range(max_capacity)]
        self.__front_ = -1
        self.__end_ = -1
        self.__size_ = 0
        self.__CAPACITY_ = max_capacity

    def AddToQueue(self, new_item):
        if self.__size_ < self.__CAPACITY_:
            if self.__size_ == 0:
                self.__front_ = 0

            self.__end_ += 1

            if self.__end_ > self.__CAPACITY_:
                self.__end_ = 0

            self.__queue_[self.__end_] = new_item
            self.__size_ += 1

        else:
            print("Queue is at max capacity, cannot take more elements")


    def RemoveItem(self):
        if  self.__size_ == 0:
            print("Queue is already empty.")

        else:
            self.__queue_[self.__front_] = None
            self.__front_ += 1
            self.__size_ -=1
            


    def PrintAllInQueue(self):
        for i in self.__queue_:
            print(i)
            
        

def Print():
    print(queue.__queue_)
queue = Queue(8)
queue.AddToQueue(12)
Print()

queue.RemoveItem()
Print()
queue.PrintAllInQueue()
