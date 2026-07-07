class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = stoneSum // 2
        dp = {0}
        
        for s in stones:
            nxt_dp = set(dp)
            for v in dp:
                if v + s == target:
                    return stoneSum - 2 * target
                if v + s < target:
                    nxt_dp.add(v + s)
            dp = nxt_dp

        return stoneSum - 2 * max(dp)