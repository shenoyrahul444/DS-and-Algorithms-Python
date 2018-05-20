# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        # Edge case check

        if headA == None or headB == None:
            return None

        m = self.getSizeOf(headA)
        n = self.getSizeOf(headB)

        # We want HeadA or m, to be longer of the 2 Linked lists
        if m < n:
            self.getIntersectionNode(headB, headA)

        # Preservation of heads
        currA = headA
        currB = headB

        for i in range(m - n):
            currA = currA.next

        # Now both the LinkedLists are of the same size. We traverse over them at the same pace until we find the intersection node OR one of them ends, which would mean there is no intersection

        while currA and currB:

            if id(currA) == id(currB):
                return currA

            currA = currA.next
            currB = currB.next

        return None

    def getSizeOf(self, root):
        n = 0

        while root:
            root = root.next
            n += 1

        return n


class Solution1(object):
    def getIntersectionNode1(self, headA, headB):

        if headA == None or headB == None:
            return None

        nodes = {}
        while headA:
            nodes[id(headA)] = headA.val
            headA = headA.next

        while headB:
            if nodes.get(id(headB), 0) == 0:
                headB = headB.next
            else:
                return headB

        return None