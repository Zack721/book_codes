class Queue:
    def __init__(self, max_capacity):
        self.queue_ = [None for i in range(max_capacity)]
        self.front_ = -1
        self.end_ = -1
        self.size_ = 0
        self.max_ = max_capacity

    def AddToQueue(self, new_item):
        if self.size_ < self.max_:
            if self.size_ == 0:
                self.front_ = 0
                self.end_ = 0

            #remember to edit for wrap around
            self.end_ += 1
            self.queue_[self.end_] = new_item

        print("Queue is at max capacity, cannot take more elements")


    def RemoveItem(self):
        if  self.
            