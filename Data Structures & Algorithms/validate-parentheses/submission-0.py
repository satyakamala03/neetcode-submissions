class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mpp = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        for c in s:
            if c in mpp.keys():
                stack.append(c)
            else:
                if not stack:
                    return False
                if not mpp[stack[-1]] == c:
                    return False
                stack.pop()
        
        return True if not stack else False
                