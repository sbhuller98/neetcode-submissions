class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = set()
        total = nums[0]

        for item in range(1, len(nums)):
            if nums[item] == 0:
                zeroes.add(item)
            else:
                total *= nums[item]

        ans = []

        if len(zeroes) > 1:
            return [0] * len(nums)
        for i in range(len(nums)):
            if len(zeroes) > 0:
                if i in zeroes:
                    ans.append(total)
                else:
                    ans.append(0)
            else: 
                ans.append(total // nums[i])
        
        return ans