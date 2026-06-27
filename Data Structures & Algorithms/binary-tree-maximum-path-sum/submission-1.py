# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxAns = -math.inf

        def recurse(nd):
            if not nd:
                return 0

            leftMax = recurse(nd.left)
            rightMax = recurse(nd.right)

            currMax = max(nd.val + leftMax, nd.val + rightMax, nd.val)
            nonlocal maxAns
            maxAns = max(maxAns, currMax, nd.val + leftMax + rightMax)
            return currMax
        
        return max(recurse(root), maxAns)