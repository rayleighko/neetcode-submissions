class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for n in nums:
            counts[n] += 1

        i, j = 0, 0
        res = []
        for count in counts:
            for c in range(count):
                nums[i] = j
                i += 1
            j += 1