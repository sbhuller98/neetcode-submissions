class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), 50000 * len(weights)
        weight = r

        while l <= r:
            m = (l + r) // 2
        
            weightSoFar = 0
            daysSoFar = 0

            for item in weights:
                if (weightSoFar + item) <= m:
                    weightSoFar += item
                else:
                    daysSoFar += 1
                    weightSoFar = item

            if weightSoFar: daysSoFar += 1
            print(m)
            print(daysSoFar)

            if daysSoFar <= days:
                weight = min(weight, m)
                r = m - 1
            else:
                l = m + 1
        
        return weight