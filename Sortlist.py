class Node:
    def __init__(self,val):
        self.value = val
        self.next = None

def sortlist(node,length):
    head = node

    # Base case
    if not node or not length:
        return False

    # Case 1 - When List has only 1 element, return as it is
    if not node.next:
        print ("List has just one element")
        return node



    for i in range(length):
        curr = head
        next = curr.next
        while curr and next:
            # print(curr.value,curr.next.value)
            if curr.value > next.value:
                if curr == head:
                    temp = next.next
                    next = curr
                    head = curr.next
                    curr.next = temp
                else:
                    temp = curr.next.next
                    curr.next.next = curr
                    curr.next = temp
            else:
                curr = curr.next

        print(head.value)


    return head


a = Node(7)
b = Node(3)
c = Node(8)
d = Node(4)
e = Node(5)
f = Node(2)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

curr = a
def printList(node):
    head = node
    curr = head
    while curr:
        print(curr.value)
        curr = curr.next

head = sortlist(a,6)
print("\n")
printList(head)
