class Solution:
    def isValid(self, s: str) -> bool:
        self.closedToOpen = {']':'[','}':'{',')':'('}
        self.stack = []

        for char in s:
            if self.stack and char in self.closedToOpen:
                if self.closedToOpen[char] == self.stack[-1]:
                    self.stack.pop()
                else: 
                    return False
            else:
                self.stack.append(char)

        return True if not self.stack else False
        