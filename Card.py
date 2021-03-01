
class Card:

	def __init__(self, suit, rank):
		self.suit = suit.upper()
		self.rank = rank.upper()
		self.count = 1
	
		self.parent = None
		self.left = None
		self.right = None
	
	def __gt__(self, other):
		ranks = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}
		if self.rank == type(str):
			self.rank = self.rank.upper()
		self.suit = self.suit.upper()

		if other.rank == type(str):
			other.rank = other.rank.upper()
		other.suit = other.suit.upper()

		if ranks[self.rank] > ranks[other.rank]:
			return True
		elif ranks[self.rank] == ranks[other.rank]:
			if self.suit > other.suit:
				return True
		
		return False
	
	def __lt__(self, other):
		ranks = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}
		if self.rank == type(str):
			self.rank = self.rank.upper()
		self.suit = self.suit.upper()

		if other.rank == type(str):
			other.rank = other.rank.upper()
		other.suit = other.suit.upper()

		if ranks[self.rank] < ranks[other.rank]:
			return True
		elif ranks[self.rank] == ranks[other.rank]:
			if self.suit < other.suit:
				return True
		
		return False

	def __eq__(self, other):
		if not other:
			return False
		elif (self.rank == other.rank) and (self.suit == other.suit):
			return True
		return False

	def __str__(self):
		return "{} {} | {}\n".format(self.suit, self.rank, self.count)

	def getSuit(self):
		return self.suit
	def setSuit(self, suit):
		self.suit = suit
	
	def getRank(self):
		return self.rank
	def setRank(self, rank):
		self.rank = rank
	
	def getCount(self):
		return self.count
	def setCount(self, count):
		self.count = count

	def getParent(self):
		return self.parent
	def setParent(self, parent):
		self.parent = parent
	
	def getLeft(self):
		return self.left
	def setLeft(self, left):
		self.left = left

	def getRight(self):
		return self.right
	def setRight(self, right):
		self.right = right

## Book helper functions ##

	def isLeftChild(self):
		return self.parent and self.parent.left == self

	def isRightChild(self):
		return self.parent and self.parent.right == self

	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not (self.right or self.left)

	def hasAnyChildren(self):
		return self.right or self.left

	def hasBothChildren(self):
		return self.right and self.left
	
	def spliceOut(self):
		if self.isLeaf():
			if self.isLeftChild():
				self.parent.left = None
			else:
				self.parent.right = None
		elif self.hasAnyChildren():
			if self.left:
				if self.isLeftChild():
					self.parent.left = self.left
				else:
					self.parent.right = self.left
				self.left.parent = self.parent
			else:
				if self.isLeftChild():
					self.parent.left = self.right
				else:
					self.parent.right = self.right
				self.right.parent = self.parent
	
	def replaceNodeData(self, suit, rank, left, right):
		suit.upper()
		rank.upper()
		self.suit = suit
		self.rank = rank
		self.left = left
		self.right = right
		if self.getLeft():
			self.left.parent = self
		if self.getRight():
			self.right.parent = self

	def findSuccessor(self):
		successor = None
		if self.getRight():
			successor = self.right.findMin()
		else:
			if self.getParent():
				if self.isLeftChild():
					successor = self.parent
				else:
					self.parent.right = None
					successor = self.parent.findSuccessor()
					self.parent.right = self
		return successor

	def findMin(self):

		current = self
		while current.getLeft():
			current = current.left
		return current