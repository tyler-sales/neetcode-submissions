class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        order = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, value in count.items():
            order[value].append(key)
        
        sol = []
        for i in reversed(range(len(order))):
            for val in order[i]:
                sol.append(val)
                if len(sol) == k:
                    return sol
        return sol