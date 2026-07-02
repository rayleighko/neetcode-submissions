class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dials = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        ans = [""]

        for d in digits:
            i = int(d) - 2
            tmp = []
            for curStr in ans:
                for c in dials[i]:
                    tmp.append(curStr + c)
            ans = tmp

        return ans