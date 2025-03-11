NULLPOINTER =-1

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.ptr_to_next= None

class HashTable:
    def __init__(self, capacity):
        self.max_capacity = capacity
        self.size = 0
        self.table = [None for i in range(capacity)]


    def __Hash(self, key):
        return hash(key) % self.max_capacity
    
    def Insert(self, key, value):
        index = self.__Hash(key)
        new_node = Node(key, value)
        
        if self.table[index] == None:
            self.table[index] = new_node
            self.size += 1
        else:
            current_node = self.table[index]
            while current_node != None:
                if current_node.key == new_node.key: 
                    current_node.value = new_node.value
                    
                    return
                current_node = current_node.ptr_to_next

            current_node.ptr_to_next = new_node
            self.size += 1

    def Search(self, key): 
        index = self.__Hash(key)
        
        current_node = self.table[index]
        while current_node != None:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.ptr_to_next

        return False

    def RemoveNode(self, key): #doesnt work properly
        index = self.__Hash(key)
        current_node = self.table[index]        
        temp = None

        while current_node != None:   #This is the part that dont work
            if current_node.key == key:  #found it 
                if temp == None:
                    self.table[index] = current_node.ptr_to_next
                    return
                
            
            temp = current_node
            



            current_node = current_node.ptr_to_next


            
        print("Not in hash table bozo")
            


if __name__ == "__main__":
    table = HashTable(8)
    table.Insert("isaac", 18)
    assert table.size == 1
    table.Insert("isaac", 20)
    assert table.size == 1
    assert table.Search("isaac") == 20
    assert table.Search("JOsias") == False

    print("Test successful")
    




    

