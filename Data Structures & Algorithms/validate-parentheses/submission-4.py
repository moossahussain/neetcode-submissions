class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        isClose = { ")" : "(", "]" : "[", "}" : "{" } 

        for c in s:
            if c in isClose:
                if stack and stack[-1] == isClose[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)


        return True if not stack else False