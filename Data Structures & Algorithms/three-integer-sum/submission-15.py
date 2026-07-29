class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l, r, m = 0, len(nums) - 1, 1
        sol = []
        scene = set()
        sNums = sorted(nums)

        while m < r:
            while m < r:
                if sNums[l] + sNums[r] + sNums[m] == 0:
                    if (sNums[l], sNums[r], sNums[m]) not in scene:
                        scene.add((sNums[l], sNums[r], sNums[m]))
                        sol.append([sNums[l], sNums[r], sNums[m]])
                    m += 1
                elif sNums[l] + sNums[r] + sNums[m] > 0:
                    r -= 1
                else:
                    m += 1   
            l += 1
            r = len(nums) - 1
            m = l + 1

        return sol