from Card import Card
from PlayerHand import PlayerHand

def test_Card():
    c1 = Card('D', 'A')
    c2 = Card('S', '2')
    c3 = Card('C', 'Q')
    c4 = Card('C', 'Q')

    assert (c1 > c2) == False
    assert (c1 < c3) == True
    assert (c3 == c2) == False
    assert (c4 == c3) == True
    assert c1.getRank() == "A"
    assert c1.getSuit() == "D"
    assert c1.getCount() == 1
    assert c1.__str__() == "D A | 1\n"

def test_constructPlayerHand():
    hand = PlayerHand()
    assert hand.root == None
    assert hand.getTotalCards() == 0

def test_getTotalCards():
    hand = PlayerHand()
    assert hand.getTotalCards() == 0
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    assert hand.getTotalCards() == 4

def test_getMin():
    hand = PlayerHand()
    hand.put('D', 'A')
    assert hand.getMin().__str__() == "D A | 1\n"
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    assert hand.getTotalCards() == 4
    assert hand.getMin().__str__() == "D A | 1\n"

def test_getSuccessor():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    assert hand.getSuccessor("D", "A").__str__() == "S 2 | 1\n"
    assert hand.getSuccessor("S", "K") == None

def test_insertRoot_PUT():
    hand = PlayerHand()
    hand.put('D', 'A')
    assert hand.root.suit == "D"
    assert hand.root.rank == "A"
    assert hand.root.getLeft() == None
    assert hand.root.getRight() == None
    assert hand.root.isLeftChild() == None
    assert hand.root.isRightChild() == None
    assert hand.root.isRoot() == True
    assert hand.root.hasAnyChildren() == None
    assert hand.root.isLeaf() == True
    assert hand.root.hasBothChildren() == None
    hand.root.replaceNodeData('S', 'K', None, None)
    assert hand.root.suit == "S"
    assert hand.root.rank == "K"

def test_insertCards_PUT():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    assert hand.root.suit  == "D"
    assert hand.root.rank  == "A"
    assert hand.root.count  == 1
    assert hand.root.right.suit == "S"
    assert hand.root.right.rank == "K"
    assert hand.root.right.count == 1
    assert hand.root.left == None
    assert hand.root.left == None
    assert hand.root.left == None
    assert hand.root.right.left.suit == "S"
    assert hand.root.right.left.rank == "2"
    assert hand.root.right.left.count == 1
    assert hand.root.right.right == None
    assert hand.root.right.right == None
    assert hand.root.right.right == None
    assert hand.root.right.left.right.suit == "C"
    assert hand.root.right.left.right.rank == "Q"
    assert hand.root.right.left.right.count == 1

def test_delete():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    assert hand.getTotalCards() == 4
    hand.delete("C", "Q")
    assert hand.getTotalCards() == 3
    hand.delete("S", "2")
    hand.delete("S", "K")
    hand.delete("D", "A")
    assert hand.getTotalCards() == 0

def test_isEmpty():
    hand = PlayerHand()
    assert hand.isEmpty() == True
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    assert hand.isEmpty() == False

def test_getCards():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    assert hand.get('D', 'A').__str__() == "D A | 1\n"
    assert hand.get('S', 'K').__str__() == "S K | 1\n"
    assert hand.get('S', '2').__str__() == "S 2 | 1\n"
    assert hand.get('C', 'Q').__str__() == "C Q | 1\n"
    assert hand.get("D", "4") == None
 
def test_inOrder():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')

    assert hand.inOrder() == \
"D A | 1\n\
S 2 | 1\n\
H 7 | 1\n\
C Q | 1\n\
C K | 1\n\
S K | 2\n"

def test_preOrder():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')

    assert hand.preOrder() == \
"D A | 1\n\
S K | 2\n\
S 2 | 1\n\
C Q | 1\n\
H 7 | 1\n\
C K | 1\n"