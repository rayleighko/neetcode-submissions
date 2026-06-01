class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # day 1 - watch solution
        # if len(s) != len(t):
        #     return False
            
        # return sorted(s) == sorted(t)
        
        # day 2 - only use my brain, but lack of exception handling
        return sorted(s) == sorted(t)