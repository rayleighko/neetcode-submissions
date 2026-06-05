class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # this is brute force, wirte only my effort.
        # output, i = [], 0
        # while i < len(nums):
        #     output.append(math.prod(nums[i+1:]) * math.prod(nums[:i]))
        #     i += 1
        # return output

        # i do write this solution after watch solution
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res