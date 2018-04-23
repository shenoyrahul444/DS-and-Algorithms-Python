class Node:
    def __init__(self,val):
        self.value = val
        self.next = None

a = Node(3)
b = Node(4)
c = Node(5)
d = Node(6)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

def removeElement(node,num):

    print("Head Value ", node.value)
    if not node or not num:
        print("Empty values in input")
        return False

    head = node
    # Check if the head needs to be removed
    if node.value == num:
        head = head.next
        return head

    # If the value to be removed is not the head
    curr = head.next
    prev = head

    while curr:
        if curr.value == num:
            prev.next = curr.next
            curr = None
            # printList(head)
            return head
        else:
            prev = curr
            curr = curr.next
            print(curr.value, prev.value)

    return False

def printList(head):

    if not head:
        print("The element is empty")
        return False

    curr = head

    while curr:
        print(curr.value)
        curr = curr.next

head = a
printList(head)
# printList(a)

print("\n\n Removing the element!!!")

head = removeElement(a,6)


print("\n\n Printing from the new head!!!")
printList(head)