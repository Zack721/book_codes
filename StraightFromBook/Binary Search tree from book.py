# NullPointer should be set to -1 if using array
element with index 0
NULLPOINTER = -1
# Declare record type to store data and pointer
class TreeNode :
 def __init__(self) :
  self.Data = ""
  self.LeftPointer = NULLPOINTER
  self.RightPointer = NULLPOINTER

def InitialiseTree() :
 Tree = [TreeNode() for i in range(8)]
 RootPointer = NULLPOINTER # set Root pointer
 FreePtr = 0 # set starting position of free list
 for Index in range(7) : # link all nodes to make free list
  Tree[Index].LeftPointer = Index + 1
 return(Tree, RootPointer, FreePtr)

def InsertNode(Tree, RootPointer, FreePtr, NewItem) :
 if FreePtr != NULLPOINTER :
  # there is space in the array
  # take node from free list and store data item
  NewNodePtr = FreePtr
  Tree[NewNodePtr].Data = NewItem
  FreePtr = Tree[FreePtr].LeftPointer
  Tree[NewNodePtr].LeftPointer = NULLPOINTER
  # check if empty tree
  if RootPointer == NULLPOINTER :
   # insert new node at root
   RootPointer = NewNodePtr
  else : # find insertion point
   ThisNodePtr = RootPointer
   while ThisNodePtr != NULLPOINTER : # while not a leaf node
    PreviousNodePtr = ThisNodePtr # remember this node
    if Tree[ThisNodePtr].Data > NewItem :
     TurnedLeft = True # follow left pointer
     ThisNodePtr = Tree[ThisNodePtr].LeftPointer
    else :
     TurnedLeft = False
     ThisNodePtr = Tree[ThisNodePtr].RightPointer
   if TurnedLeft :
    Tree[PreviousNodePtr].LeftPointer = NewNodePtr
   else :
    Tree[PreviousNodePtr].RightPointer = NewNodePtr
 else :
  print("no space for more data")
 return(Tree, RootPointer, FreePtr)

def FindNode(Tree, RootPointer, SearchItem) :
 ThisNodePtr = RootPointer # start at the root of the tree
 while ThisNodePtr != NULLPOINTER and Tree[ThisNodePtr].Data != SearchItem :
  # while there is a pointer to follow and search item not found
  if Tree[ThisNodePtr].Data > SearchItem :
   ThisNodePtr = Tree[ThisNodePtr].LeftPointer # follow left pointer
  else :
   ThisNodePtr = Tree[ThisNodePtr].RightPointer # follow right pointer
 return(ThisNodePtr)

def TraverseTree(Tree, RootPointer) :
 if RootPointer != NULLPOINTER :
  TraverseTree(Tree, Tree[RootPointer].LeftPointer)
  print(Tree[RootPointer].Data)
  TraverseTree(Tree, Tree[RootPointer].RightPointer)

def GetOption() :
 print("1: add data")
 print("2: find data")
 print("3: traverse tree")
 print("4: end program")
 option = input("Enter your choice: ")
 return(option)

Tree, RootPointer, FreePtr = InitialiseTree()
Option = GetOption()
while Option != "4" :
 if Option == "1" :
  Data = input("Enter the value: ")
  Tree, RootPointer, FreePtr = InsertNode(Tree, RootPointer, FreePtr, Data)
  TraverseTree(Tree, RootPointer)
 elif Option == "2" :
  Data = input("Enter search value: ")
  ThisNodePtr = FindNode(Tree, RootPointer, Data)
  if ThisNodePtr == NULLPOINTER :
   print("value not found")
  else :
   print("value found at ", ThisNodePtr)
  print(RootPointer, FreePtr)
  for i in range(8) :
   print(i, " ", Tree[i].LeftPointer, " ", Tree[i].Data, " ", Tree[i].RightPointer)
 elif Option == "3" :
  TraverseTree(Tree, RootPointer)
 Option = GetOption()
