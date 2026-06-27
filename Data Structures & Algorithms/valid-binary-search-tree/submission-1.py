# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recurse(curr: Optional[TreeNode], minVal: Optional[int], maxVal: Optional[int]) -> (bool, int, int):
            if not curr: return True

            if curr.val <= minVal or curr.val >= maxVal:
                return False
            
            return recurse(curr.right, curr.val, maxVal) and recurse(curr.left, minVal, curr.val)

        return recurse(root, -math.inf, math.inf)
