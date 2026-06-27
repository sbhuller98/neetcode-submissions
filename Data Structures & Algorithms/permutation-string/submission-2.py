from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        arrS1 = [0] * 26
        arrS2 = [0] * 26

        matching = 0

        for i in range(len(s1)):
            arrS1[ord(s1[i]) - ord("a")] += 1
            arrS2[ord(s2[i]) - ord("a")] += 1

        for i in range(26):
            if arrS1[i] == arrS2[i]:
                matching += 1
        
        for i in range(len(s1), len(s2)):
            if matching == 26:
                return True

            val = ord(s2[i]) - ord("a")
            if arrS2[val] == arrS1[val]:
                matching -= 1
            arrS2[val] += 1
            if arrS2[val] == arrS1[val]:
                matching += 1
            
            val = ord(s2[i - len(s1)]) - ord("a")
            if arrS2[val] == arrS1[val]:
                matching -= 1
        
            arrS2[val] -= 1
            if arrS2[val] == arrS1[val]:
                matching += 1

        return matching == 26

