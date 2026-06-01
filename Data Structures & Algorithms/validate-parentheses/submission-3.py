class Solution:
    def isValid(self, s: str) -> bool:
        # day 1 - watch solution
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

        # day 2 - watch before answer
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}
        
        for c in s:
            # is close bracket 
            if c in closeToOpen:
                # stack not empty and last item is faire c's open bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                # stack is emtpty or last item is not fair c's open bracket
                else:
                    return False
            else:
                stack.append(c)

        # stack is empty
        # if not stack:
        #     return True
        # else:
        #     return False
            
        return True if not stack else False