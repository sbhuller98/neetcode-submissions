# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ""
        curr = l1
        while curr:
            n1 += str(curr.val)
            curr = curr.next

        n2 = ""
        curr = l2
        while curr:
            n2 += str(curr.val)
            curr = curr.next

        newNum = str(int(n1[::-1]) + int(n2[::-1]))

        dummy = ListNode()
        newHead = dummy

        for char in newNum[::-1]:
            dummy.next = ListNode(int(char))
            dummy = dummy.next

        return newHead.next