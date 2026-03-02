class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                
                ch = stack.pop()
                # Check for mismatches
                if (bracket == ")" and ch != "(") or \
                   (bracket == "}" and ch != "{") or \
                   (bracket == "]" and ch != "["):
                    return False
        
        # If stack is empty, all brackets were matched correctly
        return len(stack) == 0
            