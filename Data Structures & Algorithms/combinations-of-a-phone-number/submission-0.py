class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = []

        mapping = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]

        }

        def backtrack(index, soFar):
            if index == len(digits):
                ans.append(soFar)
                return
            
            curr = digits[index]

            for mapp in mapping[curr]:
                backtrack(index + 1, soFar + mapp)
        
        backtrack(0, "")
        return ans


