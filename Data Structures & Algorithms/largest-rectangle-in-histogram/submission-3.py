class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        stack = []
        best = 0

        for i in range(n + 1):
            if i == n:
                val = 0
            else:
                val = heights[i]
            leftMost = i
            while stack and stack[-1][1] >= val:
                curr = stack.pop()
                leftMost = curr[0]
                best = max(best, (i - curr[0]) * curr[1])    
            stack.append((leftMost, val))
            if i == n-1:
                stack.append((0,0))

        return best
        