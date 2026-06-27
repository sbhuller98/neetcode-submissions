class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        direction = 1
        i,j = 0, len(numbers) -1

        while True:
            if i < 0 or j == len(numbers):
                direction = direction * -1
                continue
            total = numbers[i] + numbers[j]
            if total == target:
                return [i+1,j+1]
            if abs(i-j) == 1:
                direction = direction * -1
            elif total > target:
                
                if direction == 1:
                    j -= 1
                else:
                    j += 1
            else:
                if direction == 1:
                    i += 1
                else:
                    i -= 1

        return []