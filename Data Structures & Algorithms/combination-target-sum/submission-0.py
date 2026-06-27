class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        tupleAns = set()

        def recurse(curr):
            summation = sum(curr)
            if summation == target:
                tupleAns.add(tuple(sorted(curr)))
            elif summation < target:
                for item in nums:
                    curr.append(item)
                    recurse(curr)
                    curr.pop()
            

        recurse([])

        ans = []
        for item in tupleAns:
            ans.append(list(item))

        return ans


            


