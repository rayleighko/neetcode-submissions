class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 'l' is buy index, 'r' is sell index
        l, r = 0, 1 # Left=buy, right=sell
        maxP = 0

        while r < len(prices):
            #profitable ?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # l += 1
                l = r
            r += 1

        return maxP