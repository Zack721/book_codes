class Node:
    def __init__(self):
        self.value = None
        self.key = None
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.table = [None for i in range(capacity)]
        self.size = 0
        self.max_capacity = capacity

    def HashFunction(self, key):
        return hash(key) % self.max_capacity
    

    def Insert(self, key, value):
        index = self.HashFunction(key)

        new_node = Node()
        new_node.key = key
        new_node.value = value

        current = self.table[index]
        if current == None:
            self.table[index] = new_node
            self.size +=1
        else:
            while current != None:
                if current.key == key:
                    current.value = value
                    return
                current = current.next

            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size +=1
            

            
        

    def DeleteNode(self, key):
        index = self.HashFunction(key)

        previous = None
        current = self.table[index]

        while current != None:
            if current.key == key:
                if previous != None:
                    previous.next = current.next

                else:
                    self.table[index] = current.next
                self.size -=1
                return
            
            previous = current
            current = current.next

        print("Doesnt exist in hash table")

    def PrintHash(self):
        for i in range(self.max_capacity):
            if self.table[i] == None:
                print("None")
                #print("\n")

            else:
                current = self.table[i]
                while current != None:
                    print(f"{current.key};{current.value} =>{current.next}")
                    current = current.next
                #print("\n")

if __name__ == "__main__":
    hashtble = HashTable(8)
    hashtble.Insert("Isaac", 18)
    hashtble.Insert("Josias", 23)
    hashtble.Insert("Nathan", 23)
    hashtble.Insert("Isaac", 2006)
    hashtble.PrintHash()
    print(f"Before deleting one, the size is {hashtble.size}")
    hashtble.DeleteNode("Isaac")
    print(f"After deleting one, the size is {hashtble.size}")
    hashtble.PrintHash()

