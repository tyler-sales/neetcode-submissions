class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for char in s:
            if char in pairs:
                stack.append(pairs[char])
            elif len(stack) == 0 or stack.pop() != char:
                return False
        if len(stack) != 0:
            return False
        return True
