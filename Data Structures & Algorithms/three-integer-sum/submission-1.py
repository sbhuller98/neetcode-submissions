class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numSorterd = sorted(nums)
        ans = []

        for i in range(len(numSorterd)):
            if numSorterd[i] > 0:
                break
            if i > 0 and numSorterd[i] == numSorterd[i - 1]:
                continue

            l,r = i + 1, len(numSorterd) - 1

            while l < r:
                val = numSorterd[l] + numSorterd[r] + numSorterd[i]
                if val == 0:
                    ans.append([numSorterd[l],numSorterd[r],numSorterd[i]])
                    l += 1
                    r -= 1
                    while numSorterd[l] == numSorterd[l - 1] and l < r:
                        l += 1
                elif val > 0:
                    r -= 1
                else:
                    l += 1
        
        return ans
