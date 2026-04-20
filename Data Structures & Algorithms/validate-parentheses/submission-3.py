class Solution:
    def isValid(self, s: str) -> bool:
        
        closedToOpen = {']':'[','}':'{',')':'('}
        stack = []


        for char in s:
            if char in closedToOpen and stack:
                if stack[-1] == closedToOpen[char]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(char)

        return True if not stack else False 
