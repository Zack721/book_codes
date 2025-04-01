NULLPOINTER = -1
class Node:
    def __init__(self):
        self.data = None
        self.right_ptr = NULLPOINTER
        self.left_ptr = NULLPOINTER
        

class BinaryTree:
    def __init__(self, capacity):
        self.__tree_ = [Node() for i in range(capacity)]
        self.__root_ptr_ = NULLPOINTER
          #points to empty space in list not binary tree
        self.__size_ = 0
        self.__max_ = capacity




    def Insert(self, new_item):
        if self.__size_ != self.__max_:
           
            self.__tree_[self.__size_].data = new_item 
            index_of_new_item = self.__size_

            if self.__root_ptr_ == NULLPOINTER:  
                self.__root_ptr_ = index_of_new_item
                self.__size_+=1
                return
            
            is_right = None
            current_ptr = self.__root_ptr_
            previous_item = None#if is none is initial value, when entering second value will have the followingg syntax errror: "'NoneType' object has no attribute 'left_ptr'"   #need this i think in order to assign the pointer to the new_item properly
            while  current_ptr != NULLPOINTER:
                current_item = self.__tree_[current_ptr]
                if new_item < current_item.data:
                    previous_item = current_item
                    current_ptr = current_item.left_ptr
                    is_right = False

                elif new_item > current_item.data:
                    previous_item = current_item
                    current_ptr = current_item.right_ptr
                    is_right = True
                else:
                    
                    return

            if is_right == False: 
                previous_item.left_ptr = index_of_new_item   

            elif is_right == True:
                previous_item.right_ptr = index_of_new_item

            self.__size_ +=1
            
        else:
            print("Its full bozoooooooooooooo")

    def Find(self, item_to_find):
        current_ptr = self.__root_ptr_
        #found = False

        while current_ptr != NULLPOINTER: #and found == False: was ginna use this but dont need it
            #print("Iterated")
            current_item = self.__tree_[current_ptr]
            if current_item.data == item_to_find:
                #found = True
                return current_item
            
            elif item_to_find > current_item.data:
                current_ptr = current_item.right_ptr

            elif item_to_find < current_item.data:
                current_ptr = current_item.left_ptr

        return False
    
    def __Traverse(self, current):
        if current != NULLPOINTER :
            self.__Traverse(self.__tree_[current].left_ptr)
            print(self.__tree_[current].data)
            self.__Traverse(self.__tree_[current].right_ptr)
                        

    
    def Print(self):
        self.__Traverse(self.__root_ptr_)

if __name__ == "__main__":
    bt = BinaryTree(8)
    bt.Insert(9)
    bt.Insert(9)
    bt.Insert(7)
    bt.Insert(111)
    bt.Insert(52)
    bt.Insert(43)
    bt.Insert(213)
    bt.Insert(72)
   
    find_node = bt.Find(111)
    print(find_node)

    bt.Print() #doesnt work properly, dkw
