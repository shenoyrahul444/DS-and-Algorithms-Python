class Node:
    def __init__(self,val):
        self.value = val
        self.next = None

    def __str__(self):
        return "Value : " + str(self.value)

def printList(head):

    res = "Nodes [" + str(head.value)
    curr = head.next
    while curr:
        res += ","+ str(curr.value)
        curr = curr.next
    res += "]"
    print(res)

def mergeList(head1,head2):

    if not head1 or not head2:
        return

    return merge(head1,head2)

def merge(head1,head2):
    print(head1,head2)
    if not head1.next:
        head1.next = head2
        return head1

    if not head2.next:
        nxt = head1.next
        head1.next = head2
        head2.next = nxt
        return head1

    nxt1 = head1.next
    nxt2 = head2.next


    head1.next = head2
    head2.next = nxt1
    nxt1 = merge(nxt1, nxt2)
    return  head1


a = Node(7)
b = Node(3)
c = Node(8)
d = Node(4)
e = Node(5)
f = Node(2)
g = Node(12)
h = Node(10)
i = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
h.next = i



p = Node('P')
q = Node('Q')
r = Node('R')
s = Node('S')
t = Node('T')

p.next = q
q.next = r
r.next = s
s.next = t

printList(a)
printList(p)

lst = merge(a,p)
print("Printing Merged List!")
printList(lst)