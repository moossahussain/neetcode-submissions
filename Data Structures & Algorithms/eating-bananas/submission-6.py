class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        res = max(piles)


        while l <= r:
            k = l + (r - l) // 2

            total_hr = sum(math.ceil(p/k) for p in piles)

            if total_hr <=h:
                res = k
                r = k - 1
            else:
                l = k + 1
            

        return res