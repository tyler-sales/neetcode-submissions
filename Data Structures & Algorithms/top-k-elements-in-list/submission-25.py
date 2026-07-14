class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        count = [[] for _ in range(len(nums) + 1)]

        for num in nums: 
            frequency[num] = frequency.get(num, 0) + 1
        
        for key, value in frequency.items():
            count[value].append(key)

        sol = []
        for i in reversed(count):
            for v in i:
                sol.append(v)
                if len(sol) == k:
                    return sol