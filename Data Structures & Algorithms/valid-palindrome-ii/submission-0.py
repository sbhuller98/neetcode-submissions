class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1

        def check_palindrome(left, right, skipped):
            nonlocal s
            while left < right:
                if s[left] != s[right]:
                    if skipped:
                        return False
                    else:
                        return check_palindrome(left + 1, right, True) or check_palindrome(left, right - 1, True)
                left += 1
                right -= 1
            return True
               
            
        return check_palindrome(l, r, False)