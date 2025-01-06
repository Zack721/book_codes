class Queue:
  def __init__(self, max_capacity):
    self.queue_ = [None for i in range(max_capacity)]
    self.front_ = -1
    self.end_ = -1
    self.size_ = 0
    self.max_capacity_ = max_capacity
    


  def AddElement(self, element_to_add):
    if self.size_ < self.max_capacity_:
      if self.size_ == 0:
        self.front_ = 0
        
      self.end_ +=1
      self.size_ += 1
      self.queue_[self.end_] = element_to_add

      
    else:
      print("Already full bozo")
  
  def RemoveElement(self):
    if self.size_ == 0:
      print("The queue is empty")

    else:   #josias, im not sure if the queue will shift so that the empty space left from the removing of the first element
            #will be filled so for example if "A" is removed from queue ["A","B","C","D"] will it become ["","B","C","D"] or ["B","C","D"]
      self.queue_.pop(self.front_)
      self.queue_.insert(0, None) 
      self.size_ -= 1
      self.front_ += 1

      
queue = Queue(8)
assert queue.front_ == -1
assert queue.end_ == -1
assert queue.size_ == 0

queue.AddElement(12)

assert queue.front_ == 0
assert queue.end_ == 0
assert queue.size_ == 1

print(queue.queue_)

queue.AddElement(14)
queue.RemoveElement()
print(queue.queue_)
      
assert queue.front_ == 1
assert queue.end_ == 1
assert queue.size_ == 1
