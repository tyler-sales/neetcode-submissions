class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        low = s.lower()

        while l < r:
            while l < r and not self.isAlphaNum(low[l]):
                l += 1
            while l < r and not self.isAlphaNum(low[r]):
                r -= 1
            if low[l] != low[r]:
                return False
            l += 1
            r -= 1
        return True


    def isAlphaNum(self, c):
        val = ord(c)
        return (ord('a') <= val <= ord('z') or ord('A') <= val <= ord('Z') or ord('0') <= val <= ord('9'))
            