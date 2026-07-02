class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        coms = []
        nums = [i for i in range(1, n + 1)]
        
        def helper(i, curComs = []):
            if len(curComs) >= k:
                coms.append(curComs.copy())
                return
            if i >= n:
                return

            for j in range(i, n):
                curComs.append(nums[j])
                helper(j + 1, curComs)
                curComs.pop()
        
        helper(0)

        return coms