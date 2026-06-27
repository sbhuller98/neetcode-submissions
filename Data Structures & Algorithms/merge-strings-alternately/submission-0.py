class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""

        least = min(len(word1), len(word2))

        for i in range(least):
            ans += word1[i]
            ans += word2[i]
        
        return ans + word1[least:] + word2[least:]