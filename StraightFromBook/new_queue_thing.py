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

    
      if self.end_ > self.max_capacity_-1:
        self.end_ = 0
        #self.front_ = 0
      self.queue_[self.end_] = element_to_add
      
    else:
      print("Already full bozo")
  
  def RemoveElement(self):
    if self.size_ == 0:
      print("The queue is empty")

    else: 
      self.queue_[self.front_] = None
      #self.queue_.insert(self.front_, None) 
      self.size_ -= 1
      self.front_ += 1

if __name__ == "__main__":
  queue = Queue(8)

  for i in range(8):
    queue.AddElement(i)

  assert queue.queue_ == [0, 1, 2, 3, 4, 5, 6, 7]

  queue.RemoveElement()
  assert queue.queue_ == [None, 1, 2, 3, 4, 5, 6, 7]

  queue.AddElement(11)
  assert queue.size_ == 8
  assert queue.queue_ == [11, 1, 2, 3, 4, 5, 6, 7]

  queue.AddElement(12)
  assert queue.size_ == 8
  assert queue.queue_ == [11, 1, 2, 3, 4, 5, 6, 7]


  queue.RemoveElement()
  assert queue.size_ == 7
  assert queue.queue_ ==  [11, None, 2, 3, 4, 5, 6, 7]

  queue.RemoveElement()
  queue.size_ == 6
  assert queue.queue_ ==  [11, None, None, 3, 4, 5, 6, 7]

  queue.AddElement(13)
  assert queue.size_ == 7
  assert queue.queue_ == [11, 13, None, 3, 4, 5, 6, 7]

  
