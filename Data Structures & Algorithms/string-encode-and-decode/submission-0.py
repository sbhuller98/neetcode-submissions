class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ""
        for item in strs:
            for c in item:
                newStr = newStr + str(ord(c)) + ":"
            newStr = newStr + ","
        return newStr

    def decode(self, s: str) -> List[str]:
        ans = []

        currWord = ""
        currLetter = ""
        for c in s:
            if c == ",":
                ans.append(currWord)
                currWord = ""
            elif c == ":":
                currWord += chr(int(currLetter))
                currLetter = ""
            else:
                currLetter += c
        
        return ans