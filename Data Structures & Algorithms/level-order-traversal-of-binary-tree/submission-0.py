# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []


        def recurse(curr: Optional[TreeNode], level: int):
            if not curr:
                return
            
            if len(ans) == level:
                ans.append([curr.val])
            else:
                ans[level].append(curr.val)

            recurse(curr.left, level + 1)
            recurse(curr.right, level + 1)
        
        recurse(root, 0)
        return ans