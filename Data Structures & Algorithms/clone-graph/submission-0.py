"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}

        def recurse(curr):
            if curr.val in seen:
                return seen[curr.val]
            
            new = Node(curr.val)
            seen[new.val] = new

            for neighbor in curr.neighbors:
                new.neighbors.append(recurse(neighbor))

            return new

        if not node:
            return None
        return recurse(node)
