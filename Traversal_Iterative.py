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

def preorder_iterative(root):
    if not root:
        return

    stack = []
    curr = root
    stack.append(curr)

    while stack:
        curr = stack.pop()
        print(str(curr.value))

        if curr.rightChild:
            stack.append(curr.rightChild)
        if curr.leftChild:
            stack.append(curr.leftChild)


tree = BST()
tree.addNode(10)
tree.addNode(9)
tree.addNode(3)
tree.addNode(4)
tree.addNode(20)
tree.addNode(30)
tree.addNode(40)

preorder_iterative(tree.root)
