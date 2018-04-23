#
#
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     # @param head, a ListNode
#     # @return a ListNode
#     def sortList(self, head):
#         if head == None:
#             return None
#         counter = 0
#         temp = head
#         while temp != None:
#             temp = temp.next
#             counter += 1
#         return self.sort(head, counter)
#
#     def sort(self, head, size):
#         if size == 1:
#             return head
#         list2 = head
#         for i in range(0, size // 2):
#             list2 = list2.next
#         list1 = self.sort(head, size // 2)
#         list2 = self.sort(list2, size - size // 2)
#         return self.merge(list1, size // 2, list2, size - size // 2)
#
#     def merge(self, list1, sizeList1, list2, sizeList2):
#         dummy = ListNode(0)
#         list = dummy
#         pointer1 = 0
#         pointer2 = 0
#         while pointer1 < sizeList1 and pointer2 < sizeList2:
#             if list1.val < list2.val:
#                 list.next = list1
#                 list1 = list1.next
#                 pointer1 += 1
#             else:
#                 list.next = list2
#                 list2 = list2.next
#                 pointer2 += 1
#             list = list.next
#         while pointer1 < sizeList1:
#             list.next = list1
#             list1 = list1.next
#             pointer1 += 1
#             list = list.next
#         while pointer2 < sizeList2:
#             list.next = list2
#             list2 = list2.next
#             pointer2 += 1
#             list = list.next
#         list.next = None
#         return dummy.next
#
class Node:
    def __init__(self,val):
        self.value = val
        self.next = None

    def __str__(self):
        return str(self.value)

node = Node(1)
node.next = Node(5)
node.next.next = Node(3)
node.next.next.next = Node(2)
node.next.next.next.next = Node(4)
node.next.next.next.next.next  = Node(7)
node.next.next.next.next.next.next  = Node(9)

nodestr = "Nodes[" + str(node.value)
curr = node.next
while curr:
    nodestr += ", "+ str(curr.value)
    curr= curr.next

nodestr += "]"
print(nodestr)

def SortLinkedList(node):

    if node is None or type(node) != Node:
        return
    curr = node
    counter = 0
    while curr:
        curr= curr.next
        counter += 1

    print("Size of the LinkedList : "+ str(counter))

    return sort(node,counter)

def sort(head,size):

    #Base condition for recursion
    if size == 1:
        return head

    #



