class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countDict = {}
        arr = []
        res = []

        for num in nums:
            countDict[num] = countDict.get(num, 0) + 1


        for num, count in countDict.items():
            arr.append([count, num])

        arr.sort(reverse=True)

        for val in arr:
            if len(res) < k:
                res.append(val[1])
            else:
                return res

        return res



        