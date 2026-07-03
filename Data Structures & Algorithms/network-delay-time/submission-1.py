class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append([v, t])

        min_heap = [[0, k]]
        visit = set()
        ans = 0

        while min_heap:
            t1, n1 = heapq.heappop(min_heap)

            if n1 in visit:
                continue
            visit.add(n1)
            ans = t1

            for n2, t2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(min_heap, [t1 + t2, n2])

        return ans if len(visit) == n else -1