class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        arr = []
        res = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, freq in freq.items():
            arr.append([freq, num])

        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])

        return res

