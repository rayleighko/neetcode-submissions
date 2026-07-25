class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        mb = prices[0]

        for sell in prices:
            mp = max(mp, sell - mb)
            mb = min(mb, sell)
        return mp