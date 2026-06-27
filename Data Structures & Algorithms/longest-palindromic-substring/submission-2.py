class Solution:
    def longestPalindrome(self, s: str) -> str:
        bestSoFar = ""
        paliSet = set()
        def isPalindrome(val):
            l, r = 0, len(val) - 1
            while l <= r:
                if val[l:r + 1] in paliSet:
                    break

                if val[l] != val[r]:
                    return False
                l += 1
                r -= 1
            
            paliSet.add(val)
            
            return True
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                curr = s[i:j+1]
                if isPalindrome(curr):
                    if len(curr) > len(bestSoFar):
                        bestSoFar = curr

        return bestSoFar