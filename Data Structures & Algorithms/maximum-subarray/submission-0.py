class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        maxL, maxR = 0, 0
        l = 0

        for r in range(len(nums)):
            if curSum < 0:
                curSum = 0
                l = r
            curSum += nums[r]
            if curSum > maxSum:
                maxSum = max(maxSum, curSum)
                maxL, maxR = l, r

        return maxSum