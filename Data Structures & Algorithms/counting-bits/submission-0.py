class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        def bits(n):
            count = 0
            while n:
                n &= n - 1
                count += 1
            return count
        
        for r in range(n+1):
            res[r] = bits(r)

        return res