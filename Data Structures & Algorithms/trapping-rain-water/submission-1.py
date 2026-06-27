class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = height.copy()
        rightMax = height.copy()

        for i in range(1, len(leftMax)):
            leftMax[i] = max(leftMax[i-1], height[i])

        for i in range(len(rightMax) - 2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])

        waterSum = 0
        print()

        for i in range(len(height)):
            curr = min(leftMax[i], rightMax[i]) - height[i]
            if curr > 0:
                waterSum += curr
        
        return waterSum
        