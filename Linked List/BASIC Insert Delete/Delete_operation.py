class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def append(self,new_data):
		new_node = Node(new_data)

		if self.head == None:
			self.head = new_node
			return

		temp = self.head
		while temp.next:
		temp = temp.next

		temp.next = new_node

	def pop(self):
		temp = self.head
		while temp.next:
			prev = temp
			temp = temp.next
			prev.next =none

	def deletebegin(self):
		self.head = self.head.next

	def deletepos(self,pos):
		temp = self.head
		count = 1
		prev = temp
		while count != pos:
			prev = temp
			temp = temp.next
			count += 1

		prev.next = temp.next

	def printt(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next

if __name__ == '__main__':
l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)
l1.append(7)
l1.append(8)
l1.pop()
l1.pop()
l1.deletebegin()
l1.deletepos(3)
l1.printt()