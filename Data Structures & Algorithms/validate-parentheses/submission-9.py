class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"{": "}", "(": ")", "[": "]"}
        stack = []
        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if stack == []:
                    return False
                last = stack.pop()
                if c != pairs[last]:
                    return False
        if stack != []:
            return False
        return True