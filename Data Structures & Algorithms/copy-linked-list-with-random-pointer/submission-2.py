"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        store = defaultdict(lambda: Node(0))
        store[None] = None

        copy = head
        c1 = copy

        while copy:
            store[copy].val = copy.val
            store[copy].next = store[copy.next]
            store[copy].random = store[copy.random]
            copy = copy.next

        return store[head]
