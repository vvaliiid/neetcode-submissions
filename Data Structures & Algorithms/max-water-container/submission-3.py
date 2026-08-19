class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights) - 1 
        l, r = 0, n
        maxi = 0
        while l < r:
            current = (min(heights[l], heights[r])) * (r-l)
            maxi = max(maxi,current)

            if heights[r] >= heights[l]: 
                l+=1
            else: 
                r -=1
        return maxi