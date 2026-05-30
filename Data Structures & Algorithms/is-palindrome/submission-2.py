class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s.lower():
            if c.isalnum():
                newStr += c

        return newStr == newStr[::-1]