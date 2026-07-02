class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        curSet = []

        def helper(i):
            if i >= n:
                ans.append(curSet.copy())
                return
            
            curSet.append(nums[i])
            helper(i + 1)
            curSet.pop()

            helper(i + 1)

        helper(0)

        return ans