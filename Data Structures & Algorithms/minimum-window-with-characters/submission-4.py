from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        arrS = [0] * 52
        arrT = [0] * 52

        ans = ""

        def calculateOrdVal(ch):
            sVal = ord(ch)
            if sVal < 91:
                return sVal - ord("A")
            else:
                return sVal - ord("a") + 26

        for i in range(len(t)):
            sVal = calculateOrdVal(s[i])
            arrS[sVal] += 1
            
            tVal = calculateOrdVal(t[i])
            arrT[tVal] += 1

        matchingSize = len(set(t))


        matching = 0
        for i in range(len(arrS)):
            if arrS[i] > 0 and arrT[i] > 0 and arrS[i] >= arrT[i]:
                matching += 1
        
        i,j = 0,len(t)
        while j < len(s) + 1 and i <= j:
            print(s[i:j])
            print(matching)
        
            while matching == matchingSize:
                if ans == "" or len(ans) > j - i:
                    ans = s[i:j]
                if len(ans) == len(t):
                    return ans
                val = calculateOrdVal(s[i])

                if arrS[val] == arrT[val]:
                    matching -= 1
                arrS[val] -= 1
                i += 1

            if j >= len(s):
                j += 1
                continue
            val = calculateOrdVal(s[j])
            arrS[val] += 1
            if arrS[val] > 0 and arrS[val] == arrT[val]:
                matching += 1
            j += 1


        return ans
 