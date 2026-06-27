class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) <= 2: return max(nums)

        def findMax(shortenedNums):
            print(shortenedNums)
            mem = [0] * len(shortenedNums)
            mem[0] = shortenedNums[0]
            mem[1] = max(shortenedNums[1], shortenedNums[0])


            for i in range(2, len(shortenedNums)):
                mem[i] = max(mem[i-1], mem[i-2] + shortenedNums[i])
            
            return mem[-1]
        
        return max(findMax(nums[1:]), findMax(nums[:-1]))
                 
            