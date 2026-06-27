class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0

        l = 0
        seen = {}


        for i in range(len(s)):
            sub = s[i]
            if sub in seen:
                l = max(seen[sub] + 1, l)
            print(seen)
            seen[sub] = i
            count = max(count, i - l + 1)
            
        return count

