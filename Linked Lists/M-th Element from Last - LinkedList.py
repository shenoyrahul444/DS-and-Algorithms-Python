class Node:
    def __init__(self,val):
        self.value = val
        self.next = None

    def __str__(self):
        return "value : %d" % self.value


node = Node(1)
node.next = Node(5)
node.next.next = Node(3)
node.next.next.next = Node(2)
node.next.next.next.next = Node(4)
node.next.next.next.next.next = Node(7)
node.next.next.next.next.next.next = Node(9)

def findMthElement(node,m):

    # Edge Case
    if node is None:
        return
    # Preserving the head
    head = node

    curr = head
    prev = None

    counter = 0
    # Approach 1 => Find Length of LinkedList , 'l' and then calculate 'm' th element, and then traverse again 'l-m' elements to find the node
    #               This is O(n) + O(n) = O(2n) approach, might be inefficient for really long linkedList
    # We can have better approach

    # Approach 2 => Have 2 pointers. One following the other m nodes behind.
    #

    while curr:
        if counter == m:
            prev = head
        if counter > m:
            prev = prev.next
        curr = curr.next
        counter += 1

    if not prev:
        return None

    return prev

print(findMthElement(node,7))

