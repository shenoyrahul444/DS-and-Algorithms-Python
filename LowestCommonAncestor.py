class Node:
    def __init__(self, val):
        self.value = val
        self.rightChild = None
        self.leftChild = None

    def __str__(self):
        node_str = "Node has the value : " + str(self.value)

        if self.rightChild:
            node_str += "\nRight Child: " + str(self.rightChild.value)

        if self.leftChild:
            node_str += "\nLeft Child: " + str(self.leftChild.value)
        return node_str

class BST:

    def __init__(self):
        self.root = None

    def addNode(self,val):

        if self.root == None:
            self.root = Node(val)
            return

        self._addNode(self.root,val)

    def _addNode(self,root,val):                 # <-------------- Recursive traversal
        if root == None:
            return Node(val)

        if val > root.value:
            if not root.rightChild:
                root.rightChild = self._addNode(root.rightChild,val)
            else:
                self._addNode(root.rightChild, val)

        elif val < root.value:
            if not root.leftChild:
                root.leftChild = self._addNode(root.leftChild,val)
            else:
                self._addNode(root.leftChild, val)


    def printBST(self):
        if not self.root:
            return
        self._printBST(self.root)

    def _printBST(self,root):                   # <-------------- Recursive traversal
        if root:
            print(str(root.value))
            self._printBST(root.leftChild)

            self._printBST(root.rightChild)

def lowestCommonAncestor(root,val1,val2):

    if not root or not val1 or not val2:
        return
    interval = []
    if val2 > val1:
        interval = [val1,val2]
    else:
        interval = [val2,val1]


    curr = root

    while curr:
        if interval[0] <= curr.value <= interval[1]:
            print(str(curr.value))
            return
        elif curr.value > interval[0] and curr.value > interval[1]:
            curr = curr.leftChild
        elif curr.value < interval[0] and curr.value < interval[1]:
            curr = curr.rightChild



tree = BST()
tree.addNode(10)
tree.addNode(9)
tree.addNode(3)
tree.addNode(4)
tree.addNode(5)
tree.addNode(7)
tree.addNode(6)
tree.addNode(1)
tree.addNode(20)
tree.addNode(30)
tree.addNode(40)


lowestCommonAncestor(tree.root,1,6)