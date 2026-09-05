class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, p, r = 0, (len(nums) - 1) // 2, len(nums) - 1
        while l < r:
            print(l, p, r)
            if nums[p] == target:
                return p
            elif nums[p] < target:
                l = p + 1
                p = (l + r) // 2
            else:
                r = p - 1
                p = (l + r) // 2
        if nums[p] == target:
            return p
        return -1 