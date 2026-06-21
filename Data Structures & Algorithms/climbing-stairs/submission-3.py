class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one
        # n 2
        # A [1, 1], [1, 0]
        # B [1, 1], [1, 0]
        # 1 * 1 + 1 * 1 = 2
        # 1 * 1 + 1 * 0 = 1
        # 1 * 1 + 0 * 1 = 1
        # 1 * 1 + 0 * 0 = 1
        # R [2, 1], [1, 1]
        # r 2