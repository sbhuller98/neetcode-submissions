from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for item in strs:
            curr = [0] * 26

            for c in item:
                curr[ord(c) - ord("a")] += 1
            
            store[tuple(curr)].append(item)

        return list(store.values())