# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        
        ans = list1
        curr1 = list1
        curr2 = list2
        if list2.val < list1.val:
            ans = list2
            curr2 = curr2.next
        else:
            curr1 = curr1.next

        ans1 = ans

        while curr1 and curr2:
            if curr1.val < curr2.val:
                ans1.next = curr1
                curr1 = curr1.next
            else:
                ans1.next = curr2
                curr2 = curr2.next
            ans1 = ans1.next
        
        if curr1:
            ans1.next = curr1
        else:
            ans1.next = curr2

        return ans