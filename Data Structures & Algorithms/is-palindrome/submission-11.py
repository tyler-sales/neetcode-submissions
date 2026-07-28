class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s) - 1
        l = s.lower()

        while p1 < p2:
            while not l[p1].isalnum() and p1 < p2:
                p1 += 1
            while not l[p2].isalnum() and p1 < p2:
                p2 -= 1
            if l[p1] != l[p2]:
                return False
            else:
                p1 += 1
                p2 -= 1
        return True