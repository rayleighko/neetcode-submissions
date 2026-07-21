class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphaNum(c):
            return (ord('a') <= ord(c) <= ord('z') or
                    ord('A') <= ord(c) <= ord('Z') or 
                    ord('0') <= ord(c) <= ord('9'))
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not alphaNum(s[l]):
                l += 1
            while l < r and not alphaNum(s[r]):
                r -= 1
            print(s[l].lower(),s[r].lower())
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True

    