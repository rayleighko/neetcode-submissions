class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n = len(grid)
        visit = set()

        min_heap = [[grid[0][0], 0, 0]]
        visit.add((0, 0))

        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in dirs:
                nei_r, nei_c = r + dr, c + dc
                if nei_r < 0 or nei_c < 0 or nei_r == n or nei_c == n or (nei_r, nei_c) in visit:
                    continue
                visit.add((nei_r, nei_c))
                heapq.heappush(min_heap, [max(t, grid[nei_r][nei_c]), nei_r, nei_c])