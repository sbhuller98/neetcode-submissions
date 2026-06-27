# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def reverse(begin):
            start = begin
            prev = None


            for _ in range(k):
                store = start.next
                start.next = prev
                prev = start
                start = store
            
            return (prev, begin, start)

        foundEnd = False
        begin = None

        start = head
        prev = None
        fast = head
        carry = None
        while True:
            for i in range(k):
                if not fast:
                    foundEnd = True
                    break
                prev = fast
                fast = fast.next

            if foundEnd:
                break
            
            if not begin:
                begin, carry, start = reverse(start)
            else:
                carry.next, carry, start = reverse(start)
            
            fast = start
        
        if start:
            carry.next = start
        
        return begin
            


        
