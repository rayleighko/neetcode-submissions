class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        counter_s = Counter(s)
        counter_t = Counter(t)

        for k in counter_s.keys():
            if counter_s[k] != counter_t[k]:
                return False
        
        return True