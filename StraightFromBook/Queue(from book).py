class Node:
    def __init__(self):
        self.Data = ""
        self.Pointer = -1

Queue = [Node() for i in range(50)]
FrontOfQueue = -1
EndOfQueue = -1
StartOfFreeList = 0

for i in range(49):
    Queue[i].Pointer = i + 1
