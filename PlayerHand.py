from Card import Card

class PlayerHand:

	def __init__(self):
		self.root = None
		self.size = 0 		
	
	def getTotalCards(self):
		return self.size
		
	def getMin(self):
		if self.size == 0:
			return None
		
		current = self.root

		while current.getLeft():
			current = current.left
		return current
		
	def getSuccessor(self, suit, rank):
		suit.upper()
		rank.upper()

		card = self.get(suit, rank)
		if card:
			return card.findSuccessor()
		return None

	def put(self, suit, rank):
		suit.upper()
		rank.upper()
		card = self.get(suit, rank)

		if card:
			card.count += 1
			self.size += 1
		elif self.root:
			card = Card(suit, rank)
			self._put(card, self.root)
			self.size += 1
		else:
			card = Card(suit, rank)
			self.root = card
			self.size += 1

	def _put(self, card, currentNode):
		if card < currentNode:
			if currentNode.getLeft():
				self._put(card, currentNode.left)
			else:
				currentNode.left = card
				card.parent = currentNode

		else:
			if currentNode.getRight():
				self._put(card, currentNode.right)
			else:
				currentNode.right = card
				card.parent = currentNode

	def delete(self, suit, rank):
		suit.upper()
		rank.upper()
		card = self.get(suit, rank)
		if not card:
			return False
		if card.count > 1:
			card.count -= 1
			self.size -= 1

		elif self.size > 1:
			self.remove(card)
			self.size -= 1
		elif self.size == 1:
			self.root = None
			self.size = 0
		
		return True


	def remove(self, card):
		if card.isLeaf():# the case where the node to be deleted is a leaf
			if card == card.parent.left:
				card.parent.left = None
			elif card == card.parent.right:
				card.parent.right = None
			else:
				self.root = None

		elif card.hasBothChildren():# The case where The node to be deleted has both children
			succ = card.findSuccessor()
			card.setSuit(succ.suit)
			card.setRank(succ.rank)
			card.setCount(succ.count)
			card = succ
			succ.spliceOut()

		else: # The case where the node has one child
			if card.getLeft():
				if card.isLeftChild():
					card.left.parent = card.parent
					card.parent.left = card.left
				elif card.isRightChild():
					card.left.parent = card.parent
					card.parent.right = card.left
				elif card.isRoot():
					self.root = card.left
					self.root.parent = None
				else:
					card.replaceNodeData(card.left.suit, card.left.rank, card.left.left, card.left.right)
			else:
				if card.isLeftChild():
					card.right.parent = card.parent
					card.parent.left = card.right
				elif card.isRightChild():
					card.right.parent = card.parent
					card.parent.right = card.right
				elif card.isRoot():
					self.root = card.right
					self.root.parent = None
				else:
					card.replaceNodeData(card.right.suit, card.right.rank, card.left, card.right)

	def isEmpty(self):
		if self.root:
			return False
		return True

	def get(self, suit, rank):
		suit.upper()
		rank.upper()
		card = Card(suit, rank)

		if self.root:
			result = self._get(card, self.root)
			if result:
				return result
			else:
				return None
	
	def _get(self, card, currentNode):
		if not currentNode:
			return None
		elif card == currentNode:
			return currentNode
		elif card < currentNode:
			return self._get(card, currentNode.left)
		else:
			return self._get(card, currentNode.right)

	def preOrder(self):
		return self.preorder(self.root)
	def preorder(self, node): 
		ret = ""
		if node != None:
			ret += node.__str__()
			ret += self.preorder(node.getLeft())
			ret += self.preorder(node.getRight())
		return ret

	def inOrder(self):
		return self.inorder(self.root)
	def inorder(self, node):
		ret = ""
		if node != None:
			ret += self.inorder(node.getLeft())
			ret += node.__str__()
			ret += self.inorder(node.getRight())
		return ret