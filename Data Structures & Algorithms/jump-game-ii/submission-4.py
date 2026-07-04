class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        count = 0

        while i < len(nums) - 1:
            iteration = nums[i]
            maxSoFar = nums[i] + i
            nextI = nums[i] + i
            
            for j in range(i + 1, i + iteration + 1):
                if j == len(nums) or nextI >= len(nums) - 1:
                    break
                if maxSoFar <= j + nums[j]:
                    maxSoFar = j + nums[j]
                    nextI = j

            count += 1
            i = nextI

        return count
                