class Node:
    def __init__(self,val):
        self.value = val
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:

    def __init__(self):
        self.head = None

    def reverse(self):
        curr = self.head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev

    def recursive_reverse(self):

        #Edge case checking of head
        if self.head is None:
            return

        self.reverseUtil(self.head,None)

    def reverseUtil(self,curr,prev):

        #Base Condition for recursive calls
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return

        next = curr.next
        curr.next = prev

        self.reverseUtil(next,curr)



    def push(self,val):
        new_node = Node(val)
        new_node.next = self.head
        self.head  = new_node

    def pop(self):
        pop = self.head
        self.head = pop.next
        return pop

    def __str__(self):
        result = ""

        curr = self.head
        while curr:
            result += "%i " % curr.value
            curr = curr.next

        return result

l1 = LinkedList()
l1.push(5)
l1.push(10)
l1.push(15)
l1.push(25)
l1.push(32)

print(l1)
l1.reverse()
print(l1)
l1.recursive_reverse()
print(l1)
#
# print(l1.pop())
# print(l1.pop())
# print(l1)
