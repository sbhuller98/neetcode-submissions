# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None
        seenCount = 0
        def recurse(nd):
            if not nd:
                return
            
            recurse(nd.left)

            nonlocal seenCount
            seenCount += 1

            if seenCount == k:
                nonlocal ans
                ans = nd.val

            recurse(nd.right)

        recurse(root)
        return ans

        