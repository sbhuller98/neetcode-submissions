class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        candidates.sort()

        def recurse(curr, total, i):
            if target == total:
                ans.add(tuple(curr.copy()))
                return
            
            for j in range(i+1, len(candidates)):
                if total + candidates[j] > target:
                    return
                curr.append(candidates[j])
                recurse(curr, total + candidates[j], j)
                curr.pop()
            
        recurse([], 0, -1)
        
        return [list(lst) for lst in ans]