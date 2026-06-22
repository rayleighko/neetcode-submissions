class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
            hash = set()
            l = 0

            for r in range(len(nums)):
                if r - l > k:
                    hash.remove(nums[l])
                    l += 1
                
                if nums[r] in hash:
                    return True
                 
                hash.add(nums[r])

            return False