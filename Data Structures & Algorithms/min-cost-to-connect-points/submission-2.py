class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        
        for i in range(n):
            xi, yi = points[i]
            for j in range(i, n):
                xj, yj = points[j]

                dist = abs(xi - xj) + abs(yi - yj)

                adj[i].append((dist, i, j))
                adj[j].append((dist, j, i))

        min_heap = []
        visit = set()
        ans = 0

        for dist, i, j in adj[0]:
            heapq.heappush(min_heap, (dist, i, j))

        visit.add(0)

        while n > len(visit):
            dist1, i1, j1 = heapq.heappop(min_heap)

            if j1 in visit:
                continue

            visit.add(j1)
            ans += dist1

            for dist2, i2, j2 in adj[j1]:
                if j2 not in visit:
                    heapq.heappush(min_heap, (dist2, i2, j2))

        return ans
