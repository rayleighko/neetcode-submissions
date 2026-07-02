class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        def helper(i, cur = [], total = 0):
            if total == target:
                ans.append(cur.copy())
                return

            for j in range(i, n):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                helper(j, cur, total + nums[j])
                cur.pop()
        
        helper(0, [], 0)

        return ans