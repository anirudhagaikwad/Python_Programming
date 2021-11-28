# A Python program to demonstrate implementation of k queues in a single
# array in time and space efficient way


# Implementation of kQueues should use only one array, i.e., k queues should use the same array for storing elements. Following functions must be supported by kQueues.
# enqueue(int x, int qn) –> adds x to queue number ‘qn’ where qn is from 0 to k-1 
# dequeue(int qn) –> deletes an element from queue number ‘qn’ where qn is from 0 to k-1 

class KQueues:
	def __init__(self, number_of_queues, array_length):
		self.number_of_queues = number_of_queues
		self.array_length = array_length
		self.array = [-1] * array_length
		self.front = [-1] * number_of_queues
		self.rear = [-1] * number_of_queues
		self.next_array = list(range(1, array_length))
		self.next_array.append(-1)
		self.free = 0

	# To check whether the current queue_number is empty or not
	def is_empty(self, queue_number):
		return True if self.front[queue_number] == -1 else False

	# To check whether the current queue_number is full or not
	def is_full(self, queue_number):
		return True if self.free == -1 else False

	# To enqueue the given item in the given queue_number where
	# queue_number is from 0 to number_of_queues-1
	def enqueue(self, item, queue_number):
		if self.is_full(queue_number):
			print("Queue FULL")
			return
		next_free = self.next_array[self.free]
		if self.is_empty(queue_number):
			self.front[queue_number] = self.rear[queue_number] = self.free
		else:
			self.next_array[self.rear[queue_number]] = self.free
			self.rear[queue_number] = self.free
		self.next_array[self.free] = -1
		self.array[self.free] = item
		self.free = next_free

	# To dequeue an item from the given queue_number where
	# queue_number is from 0 to number_of_queues-1
	def dequeue(self, queue_number):
		if self.is_empty(queue_number):
			print("Queue EMPTY")
			return

		front_index = self.front[queue_number]
		self.front[queue_number] = self.next_array[front_index]
		self.next_array[front_index] = self.free
		self.free = front_index
		return self.array[front_index]
		
if __name__ == "__main__":
	# Let us create 3 queue in an array of size 10
	ks = KQueues(3, 10)
		
	# Let us put some items in queue number 2
	ks.enqueue(15, 2)
	ks.enqueue(45, 2)

	# Let us put some items in queue number 1
	ks.enqueue(17, 1)
	ks.enqueue(49, 1)
	ks.enqueue(39, 1)
		
	# Let us put some items in queue number 0
	ks.enqueue(11, 0)
	ks.enqueue(9, 0)
	ks.enqueue(7, 0)
		
	print("Dequeued element from queue 2 is {}".format(ks.dequeue(2)))
	print("Dequeued element from queue 1 is {}".format(ks.dequeue(1)))
	print("Dequeued element from queue 0 is {}".format(ks.dequeue(0)))
