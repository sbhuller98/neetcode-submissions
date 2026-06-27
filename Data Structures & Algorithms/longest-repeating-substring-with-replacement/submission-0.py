from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        highestFreq = 0
        seen = defaultdict(int)
        maxSoFar = 0

        i = 0

        for j in range(len(s)):
            val = s[j]
            seen[val] += 1
            highestFreq = max(highestFreq, seen[val])

            while (j - i + 1) > highestFreq + k:
                seen[s[i]] -= 1
                i += 1
            
            maxSoFar = max(maxSoFar, j - i + 1)


        return maxSoFar 
