class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        cur_set = []

        def helper(i):
            if i >= n:
                ans.append(cur_set.copy())
                return
            
            cur_set.append(nums[i])
            helper(i + 1)
            cur_set.pop()

            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1

            helper(i + 1)

        helper(0)
        
        return ans