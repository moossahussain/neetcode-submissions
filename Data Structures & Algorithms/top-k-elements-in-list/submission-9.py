class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # revision attempt using min-heap

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []
        for num, cnt in freq.items():
            heapq.heappush(heap, (cnt, num))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res