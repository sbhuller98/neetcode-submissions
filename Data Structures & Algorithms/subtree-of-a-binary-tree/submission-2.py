# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        tree1 = ""
        while stack:
            node = stack.pop()
            if not node:
                tree1 += "$"
                continue
            else:
                tree1 += str(node.val)
            
            stack.append(node.left)
            stack.append(node.right)

        stack = [subRoot]
        tree2 = ""
        while stack:
            node = stack.pop()
            if not node:
                tree2 += "$"
                continue
            else:
                tree2 += str(node.val)
            
            stack.append(node.left)
            stack.append(node.right)

        print(tree1)
        print(tree2)
        if tree2 in tree1: return True

        return False
        