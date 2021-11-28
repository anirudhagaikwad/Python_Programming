# A complete working Python program to find length of a
# Linked List recursively

# Node class
class Node:
	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None


	# This function is in LinkedList class. It inserts
	# a new node at the beginning of Linked List.
	def push(self, new_data):

		# 1 & 2: Allocate the Node &
		#	 Put in the data
		new_node = Node(new_data)

		# 3. Make next of new Node as head
		new_node.next = self.head

		# 4. Move the head to point to new Node
		self.head = new_node

	# This function counts number of nodes in Linked List
	# recursively, given 'node' as starting node.
	def getCountRec(self, node):
		if (not node): # Base case
			return 0
		else:
			return 1 + self.getCountRec(node.next)

	# A wrapper over getCountRec()
	def getCount(self):
		return self.getCountRec(self.head)

# Code execution starts here
if __name__=='__main__':
	llist = LinkedList()
	llist.push(1)
	llist.push(3)
	llist.push(1)
	llist.push(2)
	llist.push(1)
	print('Count of nodes is :',llist.getCount())
