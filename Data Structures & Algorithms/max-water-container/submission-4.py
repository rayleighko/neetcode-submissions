class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, 1
        res = 0
        while l < len(heights) and r < len(heights):
            if heights[l] < heights[r]:
                res = max(res, heights[l] * (r - l))
            else:
                res = max(res, heights[r] * (r - l))
            r += 1
            if r == len(heights):
                l += 1
                r = l + 1
                
        return res