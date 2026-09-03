class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers on opposite sides
        # iterating through the list
        # finding the min and the distance to calculate the amount of water
        # keeping track of the highest amount
        # either going until pointers cross or impossible to maximize more <- final step efficency gain

        l, r, w = 0, len(heights) - 1, len(heights) - 1
        maximum = 0 

        while l < r:
            if heights[l] < heights[r]:
                maximum = max(heights[l] * w, maximum)
                l += 1
            else:
                maximum = max(heights[r] * w, maximum)
                r -= 1
            w -= 1
        
        return maximum

            
        