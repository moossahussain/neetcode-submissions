class Solution:
    def isPalindrome(self, s: str) -> bool:

        newStr = ''

        for c in s:
            if c.isalnum():
                newStr += c.lower()

        reverse = newStr[::-1]
        if newStr == reverse:
            return True
        return False

        