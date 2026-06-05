class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output, i = [], 0
        while i < len(nums):
            output.append(math.prod(nums[i+1:]) * math.prod(nums[:i]))
            i += 1
        return output
