class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        count = {}

        window = 0
        res = 0

        for r in range(len(s)):
            window = r - l + 1
            count[s[r]] = count.get(s[r], 0) + 1


            while window - max(count.values()) > k:
                count[s[l]] = count.get(s[l]) - 1
                l +=1
                window -=1

            r+=1
            res = max(res,window)

        return res
