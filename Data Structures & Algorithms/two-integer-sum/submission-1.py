class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # day 1 - watch solution
        # prevMap = {}
        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in prevMap:
        #         return [prevMap[diff], i]
        #     prevMap[n] = i
        # return 

        # day 2 - watch before answer(prevMap idea), i think now, this is use value:idx mapping 
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return