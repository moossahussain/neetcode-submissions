class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        l=0
        window = 0
        res = 0

        for r in range(len(s)):

            count[s[r]] = count.get(s[r], 0) + 1
            window = r - l + 1

            while window - max(count.values()) > k:
                count[s[l]] = count.get(s[l]) - 1
                l +=1
                window -=1
                

            r +=1
            res = max(res, window)
    
        return res