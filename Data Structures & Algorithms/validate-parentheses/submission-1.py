class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')':'(', ']':'[', '}':'{'}
        stack = []

        for char in s:
            if char in closeToOpen:
                if stack and stack.pop() == closeToOpen[char]:
                    pass
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False

        