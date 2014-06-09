class Queue():
	def  __init__(self,enqueue,dequeue=0):
		self.dataStore = []
		self.enqueue = enqueue
		self.dequeue = dequeue
		self.front = front
		self.back = back
		self.toString = toString
		self.empty = empty

	def enqueue(element):
		self.dataStore.push(element)

	def front():
		print self.dataStore[0]

	def back():
		print self.dataStore[self.dataStore.length-1]

	def toString():
		retStr = ""
		for i in range(dataStore.length):
			retStr += self.dataStore[i] + "\n"

		print retStr

	def empty():
		if (self.dataStore.length == 0):
			print true

		else:
			print false

	def dequeue():
		print self.dataStore.pop(0)


q = Queue("Meredith")
q.enqueue("Meredith")
q.enqueue("Cynthia")
q.enqueue("Jennifer")
print(q.toString())
q.dequeue()
print(q.toString())
print("Front of queue: " + q.front())
print("Back of queue: " + q.back())