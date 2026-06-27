# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True

        def recurse(node):
            if not node:
                return 0
            
            left = recurse(node.left)
            right = recurse(node.right)

            print(abs(left-right))
            if abs(left - right) > 1:
                nonlocal result 
                result = False

            return 1 + max(left, right)
        
        recurse(root)
        return result