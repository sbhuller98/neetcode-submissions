class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []

        for item in asteroids:
            while ans and ans[-1] > 0 and item < 0:
                if abs(item) > abs(ans[-1]):
                    ans.pop()
                elif abs(item) == abs(ans[-1]):
                    ans.pop()
                    item = 0
                else:
                    item = 0
            if item:
                ans.append(item)
        return ans
                

