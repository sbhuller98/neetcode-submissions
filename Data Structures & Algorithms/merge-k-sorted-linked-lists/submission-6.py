# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not lists[0]:
            return None

        heap = []

        for item in lists:
            while item:
                heapq.heappush(heap, item.val)
                item = item.next
          
        dummy = ans = ListNode()

        while heap:
            item = heapq.heappop(heap)
            ans.next = ListNode(item)
            ans = ans.next

        return dummy.next
