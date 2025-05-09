class Node: 
	def __init__(self, key, value): 
		self.key = key 
		self.value = value 
		self.next = None


class HashTable: 
	def __init__(self, capacity): 
		self.capacity = capacity 
		self.size = 0
		self.table = [None] * capacity 

	def _hash(self, key): 
		return hash(key) % self.capacity 

	def insert(self, key, value): #gonna need detailed explanation about this especially the while loop
		index = self._hash(key) 

		if self.table[index] is None: 
			self.table[index] = Node(key, value) 
			self.size += 1
		else: 
			current = self.table[index] 
			while current: 
				if current.key == key: 
					current.value = value 
					return
				current = current.next
			new_node = Node(key, value) 
			new_node.next = self.table[index] 
			self.table[index] = new_node 
			self.size += 1

	def search(self, key): 
		index = self._hash(key) 

		current = self.table[index] 
		while current: 
			if current.key == key: 
				return current.value 
			current = current.next

		raise KeyError(key) 

	def remove(self, key): 
		index = self._hash(key)    #get the index of the node we want to remove

		previous = None                   #holds the previous node
		current = self.table[index]        #is the current node 

		while current != None:    #while the current node is not none meaning while there are still iterating through the linked list
			if current.key == key:          #if the current node is the one we want to remove
				if previous != None:         #if there is a previous is not none
					previous.next = current.next   #node1 ptr to node3 ptr basically
				else:                              #if previous node is none (menas that the first node is the one  that will be deleted)
					self.table[index] = current.next     #add second node is new first node

				self.size -= 1      # -1 size cuz removed a node
				return
			previous = current            #this and next like is for iteration
			current = current.next

		raise KeyError(key) 

	def __len__(self): 
		return self.size 

	def __contains__(self, key): 
		try: 
			self.search(key) 
			return True
		except KeyError: 
			return False


# Driver code 
if __name__ == '__main__': 

	# Create a hash table with 
	# a capacity of 5 
	ht = HashTable(5) 

	# Add some key-value pairs 
	# to the hash table 
	ht.insert("apple", 3) 
	ht.insert("banana", 2) 
	ht.insert("cherry", 5) 

	# Check if the hash table 
	# contains a key 
	print("apple" in ht) # True 
	print("durian" in ht) # False 

	# Get the value for a key 
	print(ht.search("banana")) # 2 

	# Update the value for a key 
	ht.insert("banana", 4) 
	print(ht.search("banana")) # 4 

	ht.remove("apple") 
	# Check the size of the hash table 
	print(len(ht)) # 3 
