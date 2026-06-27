class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        stack = []
        best = 0

        for i, val in enumerate(heights):
            leftMost = i
            while stack and stack[-1][1] >= val:
                curr = stack.pop()
                leftMost = curr[0]
                best = max(best, (i - curr[0]) * curr[1])
            stack.append((leftMost, val))

        while stack:
            curr = stack.pop()
            best = max(best, (n - curr[0]) * curr[1])
        return best


            
        