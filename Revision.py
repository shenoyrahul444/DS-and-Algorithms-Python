# Reverse a Singly LinkedList

class Node:
    def __init__(self,val):
        self.value = val
        self.next = None

    def __str__(self):
        return "Value : " + str(self.value)

def reverse(head):
    if not head:
        return

    prev = None
    curr = head

    return _reverse_recursive(prev,curr)

def _reverse_recursive(prev,curr):
    if not curr:
        return prev

    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

    return _reverse_recursive(prev,curr)

def lprint(head):
    if not head:
        return
    curr = head
    rev_str = ""
    while curr:
        rev_str += " "+ str(curr.value)
        curr = curr.next
    print(rev_str)


nd = Node(3)
nd.next = Node(5)
nd.next.next = Node(7)
nd.next.next.next = Node(9)
nd.next.next.next.next = Node(1)

lprint(nd)
head = reverse(nd)
print("After reversing!")
lprint(head)

