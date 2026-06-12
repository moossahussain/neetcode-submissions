class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i = 0
        j = len(heights) - 1

        area = 0

        while i < j:

            ar = (j - i) * min(heights[i], heights[j])
            
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -=1
            area = max(area, ar)

        return area


        