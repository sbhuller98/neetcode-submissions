# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def areTreesEqual(tree1 : Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
            if not tree1 and not tree2:
                return True
            
            if not tree1 or not tree2: 
                return False

            if tree1.val != tree2.val:
                return False

            return areTreesEqual(tree1.left, tree2.left) and areTreesEqual(tree1.right, tree2.right)

        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val == subRoot.val:
                if areTreesEqual(node, subRoot): return True
            
            stack.append(node.left)
            stack.append(node.right)

        return False
        