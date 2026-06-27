# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        q = [(root, -math.inf, math.inf)]

        while q:
            curr, minVal, maxVal = q.pop()
            if not curr:
                continue

            if not (minVal < curr.val < maxVal):
                return False
        
            q.append((curr.right, curr.val, maxVal))
            q.append((curr.left, minVal, curr.val))

        return True
