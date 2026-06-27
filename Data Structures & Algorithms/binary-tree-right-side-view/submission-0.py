# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans  = []

        q = collections.deque()

        q.append(root)

        while q:
            val = None
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    val = curr.val
                    q.append(curr.left)
                    q.append(curr.right)
            
            if val:
                ans.append(val)
    
        return ans
