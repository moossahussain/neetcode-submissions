class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        if len(s) != len(t):
            return False

        for char in s:
            countS[char] = countS.get(char, 0) +1
        for char in t:
            countT[char] = countT.get(char, 0) +1

        return True if countS == countT else False
