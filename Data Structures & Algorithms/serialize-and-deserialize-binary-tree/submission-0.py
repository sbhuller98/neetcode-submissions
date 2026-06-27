# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []

        def recurse(nd):
            if not nd:
                ans.append(None)
                return
            ans.append(nd.val)
            recurse(nd.left)
            recurse(nd.right)
        
        recurse(root)
        if not ans:
            return ""
        return ",".join(str(x) for x in ans)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        traversal = data.split(",")
        print(traversal)

        if not traversal:
            return None
        
        def recurse(index):
            print(index)
            if index >= len(traversal):
                return (None, index)
            print(traversal[index])
            if traversal[index] == "None":
                return (None, index)
            newNode = TreeNode(int(traversal[index]))
            newNode.left, newIndex = recurse(index + 1)
            newNode.right, finalIndex = recurse(newIndex + 1)
            return newNode, finalIndex
        
        return recurse(0)[0]
            

