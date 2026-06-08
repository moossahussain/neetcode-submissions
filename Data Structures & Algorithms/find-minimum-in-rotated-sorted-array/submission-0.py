class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1      # min strictly right of m
            else:
                r = m          # min at m or left
        return nums[l]