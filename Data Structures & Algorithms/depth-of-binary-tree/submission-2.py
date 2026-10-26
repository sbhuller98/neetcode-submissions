# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxDepth = 0
        depth = 0
        
        q = [(root, 1)]

        while q:
            rt, dp = q.pop()
            if not rt:
                continue
            q.append((rt.right, dp + 1))
            q.append((rt.left, dp + 1))
            maxDepth = max(dp, maxDepth)

        return maxDepth


