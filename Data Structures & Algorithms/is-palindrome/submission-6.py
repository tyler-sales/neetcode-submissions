class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1
        l = s.lower()

        while p1 < p2:
            if not l[p1].isalnum():
                p1 += 1
            elif not l[p2].isalnum():
                p2 -= 1
            elif l[p1] != l[p2]:
                return False
            else:
                p1 += 1
                p2 -= 1
        return True