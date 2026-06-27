class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numscopy = nums.copy()
        numscopy.sort()

        i, j = 0, len(nums) - 1

        ans = []

        while i < j:
            if numscopy[i] + numscopy[j] == target:
                ans = [numscopy[i], numscopy[j]]
                break
            elif numscopy[i] + numscopy[j] > target:
                j -= 1
            else:
                i += 1

        finalAns = []
        for i, num in enumerate(nums):
            if num == ans[0]:
                finalAns.append(i)
                break

        for i, num in enumerate(nums):
            if num == ans[1] and i != finalAns[0]:
                finalAns.append(i)
                break    

        print("here")
        print(finalAns)
        finalAns.sort()
        return finalAns
