from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for st in strs:
            arr = [0] * 26
            for letter in st:
                arr[ord(letter) - ord('a')] += 1
            seen[tuple(arr)].append(st)
        
        ans = []
        for key,val in seen.items():
            ans.append(val)

        return ans