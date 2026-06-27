# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def recurse(curr, maxSoFar):
            if not curr:
                return
            
            if curr.val >= maxSoFar:
                nonlocal count
                count += 1

            newMax = max(maxSoFar, curr.val)

            recurse(curr.left, newMax)
            recurse(curr.right, newMax)

        recurse(root, -math.inf)
        return count 