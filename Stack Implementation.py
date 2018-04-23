
# Stack Implementation using Linked List
"""
methods - __init__(),push() , pop(), __len__(), printStack()
"""
class Node:
    def __init__(self,val):
        self.value = val
        self.next = None
    def __str__(self):
        return str(self.value)

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,val):
        node = Node(val)

        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
        print("%s has been added to the list" %(val))
    def pop(self):

        if not self.head:
            print("Empty Stack")
            return False

        node = self.head
        self.head = self.head.next
        self.size -= 1
        print("%s has been removed from the list" % str(node.value))
        return node

    def __len__(self):
        return self.size

    def __str__(self):
        curr = self.head
        value_string = ""
        while curr:
            value_string = str(curr.value) +" " + value_string
            curr = curr.next
        return  value_string

names = Stack()
names.push("Rahul")
names.push("Urvi")

print(names)
print(len(names))
popped = names.pop()
print(popped)
print(names)
print(len(names))
popped = names.pop()
print(popped)
print(names)
print(len(names))
popped = names.pop()
print(popped)
print(names)