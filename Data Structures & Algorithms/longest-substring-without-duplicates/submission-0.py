class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0

        i,j = 0, 0
        seen = set()


        while j < len(s):
            if s[j] in seen:
                print(s[j])
                while True:
                    val = s[i]
                    i += 1
                    if val == s[j]:
                        break
                    seen.remove(val)
            else:
                seen.add(s[j])
            count = max(count, j - i + 1)
            j += 1
            
        return count

