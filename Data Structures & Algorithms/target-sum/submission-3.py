class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for n in nums:
            nxt_dp = defaultdict(int)
            for total, count in dp.items():
                nxt_dp[total + n] += count
                nxt_dp[total - n] += count
            dp = nxt_dp

        return dp[target]