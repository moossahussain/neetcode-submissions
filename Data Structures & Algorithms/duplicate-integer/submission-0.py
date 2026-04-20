class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashm = {}
        for i in nums:
            if i in hashm:
                return True
            else:
                hashm[i] = i
        return False
        