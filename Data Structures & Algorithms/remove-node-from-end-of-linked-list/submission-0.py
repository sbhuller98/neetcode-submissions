# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr, prev = head, head

        while curr.next != None:
            if count < n:
                count += 1
                curr = curr.next
            else:
                curr = curr.next
                prev = prev.next

        if count < n:
            return head.next
        prev.next = prev.next.next
        return head