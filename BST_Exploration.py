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
            root = Node(val)
            return root
        if val > root.value:
            root.rightChild = self._addNode(root.rightChild,val)
            return root
        elif val < root.value:
            root.leftChild = self._addNode(root.leftChild,val)
            return root

    def printBST(self):
        if not self.root:
            return
        self._printBST(self.root)

    def _printBST(self,root):                   # <-------------- Recursive traversal
        if root:
            self._printBST(root.leftChild)
            print(str(root.value))
            self._printBST(root.rightChild)


tree = BST()
tree.addNode(10)
tree.addNode(9)
tree.addNode(3)
tree.addNode(4)
tree.addNode(20)
tree.addNode(30)
tree.addNode(40)

# curr = tree.root
# while curr:
#     print(str(curr.value))
#     curr = curr.rightChild
tree.printBST()
