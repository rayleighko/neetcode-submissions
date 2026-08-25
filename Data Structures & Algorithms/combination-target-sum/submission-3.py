class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, path = [], []
        n = len(nums)
        nums.sort()

        def backtrack(start):
            total = sum(path)
            if total == target:
                res.append(path[:])
                return
                
            for i in range(start, n):
                if total + nums[i] > target:
                    return
                path.append(nums[i])
                backtrack(i)
                path.pop()

        backtrack(0)

        return res