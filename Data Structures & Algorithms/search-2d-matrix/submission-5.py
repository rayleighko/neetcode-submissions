class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for col in matrix:
        #     if target in col:
        #         return True

        # return False
        for i in range(len(matrix)):
            if target not in matrix[i]:
                continue
            l, r = 0, len(matrix[i]) - 1
            while l <= r:
                m = (l + r) // 2
                if target < matrix[i][m]:
                    r = m - 1
                elif target > matrix[i][m]:
                    l = m + 1
                else: 
                    return True

        return False