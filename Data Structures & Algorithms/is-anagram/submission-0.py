from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = defaultdict(int)
        dictt = defaultdict(int)

        for character in s:
            dicts[character] +=1
        
        for character in t:
            dictt[character] +=1
        
        if dictt == dicts:
            return True

        return False