class Solution:
    def isPalindrome(self, s: str) -> bool:

        # string reverse method

        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()

        return newStr == newStr[::-1]
        