
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            # Use .get() and [] for dictionaries
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # Update maxf inside the for loop
            maxf = max(maxf, count[s[r]])

            # This while loop MUST be inside the for loop
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1   # Square brackets here
                l += 1
            
            # Use max() to keep the largest value
            res = max(res, r - l + 1)
            
        return res