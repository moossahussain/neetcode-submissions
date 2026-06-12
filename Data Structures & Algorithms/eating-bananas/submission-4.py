class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        res = r

        while l < r:
            k = l + (r - l) // 2
            total = sum(math.ceil(p/k) for p in piles)

            if total <= h:
                r = k
            else:
                l = k + 1


        return r