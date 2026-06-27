class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def recurse(curr, open, closed):
            if closed == n:
                ans.append(curr)
            elif open == n:
                while closed < n:
                    curr += ")"
                    closed += 1
                ans.append(curr)
            else:
                if curr and open > closed:
                    recurse(curr + ")", open, closed + 1)
                recurse(curr + "(", open + 1, closed)
        
        recurse("", 0, 0)

        return ans


       