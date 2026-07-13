import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in range(len(nums)):
            if i == 0:
                products.append(math.prod((nums[1:])))
            elif i == len(nums) - 1:
                products.append(math.prod(nums[:len(nums) - 1]))
            else:
                products.append(math.prod(nums[:i] + nums[i+1:]))
        return products