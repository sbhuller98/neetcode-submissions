class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        currLongest = strs[0]

        for i in range(1, len(strs)):
            curr = ""
            length = len(currLongest)
            for i, letter in enumerate(strs[i]):
                if i < length and letter == currLongest[i]:
                    curr = curr + letter
                else:
                    break
            currLongest = curr

        return currLongest

