class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            leftChar = s[left].lower()
            leftOrd = ord(leftChar)

            rightChar = s[right].lower()
            rightOrd = ord(rightChar)        

            if not (leftOrd >= 48 and leftOrd <= 57 or leftOrd >= 97 and leftOrd <= 122):
                left += 1
            elif not (rightOrd >= 48 and rightOrd <= 57 or rightOrd >= 97 and rightOrd <= 122):
                right -= 1
            elif leftChar != rightChar: return False
            else:
                left += 1
                right -= 1
            
        return True