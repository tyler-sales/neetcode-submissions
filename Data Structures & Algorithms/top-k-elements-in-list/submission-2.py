class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        for key, value in hm.items():
            freq[value].append(key)
        
        sol = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                sol.append(n)
                if len(sol) == k:
                    return sol