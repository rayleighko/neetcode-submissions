class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        ALPHA = 26
        s1_count, s2_count = [0] * ALPHA, [0] * ALPHA

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        match = 0
        for i in range(ALPHA):
            match += (1 if s1_count[i] == s2_count[i] else 0)
            
        l = 0
        for r in range(len(s1), len(s2)):
            if match == ALPHA:
                return True

            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                match += 1
            elif s1_count[index] + 1 == s2_count[index]:
                match -= 1
            
            index = ord(s2[l]) - ord('a')
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                match += 1
            elif s1_count[index] - 1 == s2_count[index]:
                match -= 1
            l += 1

        return match == 26