class Node:
    def __init__(self,val):
        self.value = val
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def addNode(self,val):

        if self.root == None:
            self.root = Node(val)
        else:
            curr = self.root
            while curr:

                if curr.value > val:
                    if curr.left == None:
                        curr.left = Node(val)
                        break
                    else:
                        curr = curr.left
                elif curr.value < val:
                    if curr.right == None:
                        curr.right = Node(val)
                        break
                    else:
                        curr = curr.right
                elif curr.value == val:
                    if curr.right != None:
                        nxt = curr.right
                        nd = Node(val)
                        curr.right = nd
                        nd.right = nxt
                        break
                    else:
                        curr.right = Node(val)
                        break

    def printNodes(self):

        if self.root == None:
            print("There are no elements in the room!")
            return None

        self.inorder_traversal(self.root)

    def inorder_traversal(self,root):
        if root:
            print(root.value)
            self.inorder_traversal(root.left)

            self.inorder_traversal(root.right)

    def deleteNode(self,val):

        if self.root == None:
            print("The tree is already empty")
            return None

        curr = self.root
        prev = None

        while curr != None:
            if curr.value > val:
                prev = curr
                curr = curr.left
            elif curr.value < val:
                prev = curr
                curr = curr.right
            elif curr.value == val:
                break


        isRoot = False
        if prev == None and curr == self.root:
            isRoot = True

        isRightChild = False
        if isRoot == False:
            if prev.right == curr:
                isRightChild = True
        """
        There can be 3 cases
        Case 1> Node is a leaf
        Case 2> Node has 1 child
        Case 3> Node has 2 children
        """

        """ Case 1 """
        if curr.right == None and curr.left == None:
            if isRoot:
                node = self.root
                self.root = None
                return
            else:
                if isRightChild:
                    node = curr
                    prev.right = None
                    curr = None
                    return
                else:
                    node = curr
                    prev.left = None
                    curr = None
                    return

        """ Case 2 """
        if (curr.right != None and curr.left == None) or (curr.left != None and curr.right == None):

            if isRoot:
                if isRightChild:
                    self.root = curr.right
                    curr = None
                    return
                else:
                    self.root = curr.left
                    curr = None
                    return
            else:
                if isRightChild:
                    nxt = curr.right
                    prev.right = nxt
                    curr = None
                    return
                else:
                    nxt = curr.left
                    prev.left = nxt
                    curr = None
                    return


        """ Case 3 """
        if curr.right != None and curr.left!= None:
            nxt = curr.right

            if nxt.left == None:
                if isRoot:
                    nxt.left = curr.left
                    self.root = nxt
                    curr = None
                else:
                    if isRightChild:
                        nxt.left = curr.left
                        prev.right = nxt
                        curr = None
                        return
                    else:
                        nxt.left = curr.left
                        prev.left = nxt
                        curr = None
                        return

            else:
                node = self._findLargestRightSubtree(curr,curr.left)
                node.left = curr.left
                node.right = curr.right
                if isRoot:
                    curr = None
                    return
                else:
                    if isRightChild:
                        prev.right = node
                        curr = None
                        return
                    else:
                        prev.left = node
                        curr = None
                        return

    def _findLargestRightSubtree(self,prev, curr):
        if curr.left == None:
            if curr.right != None:
                prev.left = curr.right
                return curr
            else:
                prev.left = None
                return curr
        else:
            return self._findLargestRightSubtree(curr,curr.left)









tree = BST()
tree.addNode(20)
tree.addNode(30)
tree.addNode(70)
tree.addNode(25)
tree.addNode(10)
tree.addNode(15)
tree.addNode(5)
tree.printNodes()
tree.deleteNode(5)
tree.deleteNode(25)
tree.deleteNode(20)
print("\n")
tree.printNodes()

