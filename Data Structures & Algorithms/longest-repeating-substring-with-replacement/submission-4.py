class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        l = 0
        max_len = 0
        for r in range(len(s)):
            seen[s[r]] += 1
            while r - l - max(seen.values(), default=0) + 1 > k:
                seen[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len

                

            