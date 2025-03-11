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
        else:
            while current.next != None:
                current = current.next
            current.next = new_node
        self.size += 1

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


if __name__ == "__main__":
    hashtble = HashTable(8)
    hashtble.Insert("Isaac", 18)
    hashtble.Insert("Josias", 23)
    hashtble.Insert("Nathan", 23)
    hashtble.Insert("Isaac", 2006)
    print(f"Before deleting one, the size is {hashtble.size}")
    hashtble.DeleteNode("Isaac")
    print(f"After deleting one, the size is {hashtble.size}")

