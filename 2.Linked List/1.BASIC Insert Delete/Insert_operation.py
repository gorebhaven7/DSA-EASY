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
		while(temp.next != None):
		temp = temp.next

		temp.next = new_node

	def push(self,new_data):
		new_node = Node(new_data)

		new_node.next = self.head

		self.head = new_node

	def insertafter(self,key,new_data):
		new_node = Node(new_data)
		temp = self.head
		while temp != None:
			if temp.data == key:
				new_node.next = temp.next
				temp.next = new_node
				break
		temp = temp.next

	def insertat(self,prev_node,new_data):
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node


	def printt(self):
		temp = self.head
		while(temp != None):
			print(temp.data)
			temp = temp.next

if __name__ == '__main__':
l1 = LinkedList()
l1.append(4)
l1.append(5)
l1.append(8)
l1.append(9)
l1.push(3)
l1.push(1)
l1.push(0)
l1.insertafter(5,6)
l1.insertafter(6,7)
l1.insertat(l1.head.next,2)
l1.printt()
