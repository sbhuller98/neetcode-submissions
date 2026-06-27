# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not lists[0]:
            return None

        newAns = ListNode()
        copy = newAns

        while True:
            minItem = None
            minList = None
            for i, item in enumerate(lists):
                if item and (not minItem or item.val < minItem.val):
                    minItem = item
                    minList = i
            
            if not minItem:
                break

            lists[minList] = lists[minList].next

            newAns.next = minItem
            newAns = newAns.next     
            
        return copy.next
