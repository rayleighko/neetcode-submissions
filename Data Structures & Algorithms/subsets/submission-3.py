class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # not duplicated
        res, path = [], []
        n = len(nums)
        def backtracking(start):
            res.append(path[:])
            for i in range(start, n):
                path.append(nums[i])
                backtracking(i + 1)
                path.pop()
        backtracking(0)
        return res