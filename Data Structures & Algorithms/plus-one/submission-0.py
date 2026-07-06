from collections import deque

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = deque()
        carry = 0
        
        for i in range(len(digits)-1, -1, -1):
            val = digits[i] + carry
            if i == len(digits) - 1:
                val += 1
            carry = val // 10
            val -= carry * 10
            ans.appendleft(val)
        
        if carry:
            ans.appendleft(carry)
        return list(ans)
