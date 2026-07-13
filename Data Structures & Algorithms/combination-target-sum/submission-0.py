class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        def dfs(i, cur, target):
            # base case
            if target == 0:
                res.append(cur)
            elif i >= len(nums) or target < 0:
                return 0
            else:
                dfs(i+1, cur, target)
                dfs(i, cur + [nums[i]], target - nums[i])

        dfs(0, [], target)
        return res