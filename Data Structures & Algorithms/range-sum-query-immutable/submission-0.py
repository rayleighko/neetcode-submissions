class NumArray:

    def __init__(self, nums: List[int]):
        self.totalSums = []
        total = 0
        for n in nums:
            total += n
            self.totalSums.append(total)
        
    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.totalSums[right]
        leftSum = self.totalSums[left - 1] if left > 0 else 0
        return (rightSum - leftSum)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)