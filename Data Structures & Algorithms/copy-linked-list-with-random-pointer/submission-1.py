"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newHead = Node(0)
        newCopy = newHead

        copy = head

        store = {}

        while copy:
            newN = Node(copy.val)
            store[copy] = newN
            newCopy.next = newN
            newCopy = newCopy.next
            copy = copy.next

        copy = head
        newCopy = newHead.next

        while copy:
            if copy.random:
                newCopy.random = store[copy.random]
            else:
                newCopy.random = None
            
            copy = copy.next
            newCopy = newCopy.next

        return newHead.next

