# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow = head
        fast = head

        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        def reverse(start):
            prev = None

            while start:
                carry = start.next
                start.next = prev
                prev = start
                start = carry
        
            return prev
        
        if prev:
            prev.next = None
        newHead = reverse(slow)


        while head.next and newHead.next:
            carry = head.next
            head.next = newHead
            newHead = newHead.next
            head.next.next = carry
            head = carry
        
        if newHead and head:
            head.next = newHead
        

        




        
            