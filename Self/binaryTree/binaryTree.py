class Node:

	def __init__(self,key): #コンストラクタ
		self.key = key
		self.left = None
		self.right = None
		self.parent = None


class BinTree:

	def __init__(self): #コンストラクタ
		self.root = None

	def add_node(self,key,node=None):

		if node is None:
			node = self.root

		if self.root is None:
			self.root = Node(key)

		else:
			if key <= node.key:
				if node.left is None:
					node.left = Node(key)
					node.left.parent = node
					print("left")
					return
				else:
					# return self.add_node(key,node = self.root.left)
					return self.add_node(key,node = node.left)
			else:
				if node.right is None:
					node.right = Node(key)
					node.right.parent = node
					print("right")
					return
				else:
					# return self.add_node(key,node = self.root.right)
					return self.add_node(key,node = node.right)

t=BinTree()  #インスタンス生成
t.add_node(10)
t.add_node(13)
t.add_node(14)
t.add_node(8)
t.add_node(9)
t.add_node(7)
t.add_node(11)
t.add_node(80)
