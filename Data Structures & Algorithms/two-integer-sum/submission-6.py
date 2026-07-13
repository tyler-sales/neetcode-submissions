class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        order = {}
        for index, num in enumerate(nums):
            if target - num in order:
                return [order[target - num], index]
            order[num] = index
        return False