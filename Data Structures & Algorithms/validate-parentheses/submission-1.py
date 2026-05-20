class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesisMap = { ")" : "(",
                            "]" : "[",
                            "}" : "{"
                        }
        
        for c in s:
            if c in parenthesisMap: 
                if stack and stack[-1] == parenthesisMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False