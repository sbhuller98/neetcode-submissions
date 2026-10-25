class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrS = [0] * 26
        arrT = [0] * 26

        def countLetters(word, arr):
            for w in word:
                arr[ord(w) - ord('a')] += 1
            return arr

        return countLetters(s, arrS) == countLetters(t, arrT)