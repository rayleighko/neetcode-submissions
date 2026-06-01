class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for num in nums:
            hashSet.add(num)

        return len(hashSet) != len(nums)