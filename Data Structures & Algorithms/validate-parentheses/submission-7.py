class Solution:
    def isValid(self, s: str) -> bool:
        openers = {"(", "{", "["}
        pairs = {"()", "{}", "[]"}
        stack = []

        for c in s:
            if c in openers:
                stack.append(c)
            else:
                if stack == []:
                    return False
                pair = stack.pop() + c
                if pair not in pairs:
                    return False
        if stack == []:
            return True
        return False