from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    pass
    res = nums[0]
    for i in range(len(nums) - 1):
        res += nums[i + 1]
    return res

def get_min(nums: List[int]) -> int:
    pass
    res = nums[0]
    for i in range(len(nums) - 1):
        res = min(res,nums[i + 1])
    return res
def get_max(nums: List[int]) -> int:
    pass
    res = nums[0]
    for i in range(len(nums) - 1):
        res = max(res,nums[i + 1])
    return res

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
