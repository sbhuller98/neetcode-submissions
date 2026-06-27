class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)

        leftMax = [-1] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMax[i] = stack[-1]
            stack.append(i)

        rightMax = [n] * n
        stack = []
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMax[i] = stack[-1]
            stack.append(i)

        best = 0

        for i in range(n):
            best = max(best, (rightMax[i] - leftMax[i] - 1) * heights[i])
        return best
        