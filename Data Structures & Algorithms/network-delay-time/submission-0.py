class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append([v, t])

        min_heap = [[0, k]]
        visit = set()
        ans = 0

        while min_heap:
            time1, node1 = heapq.heappop(min_heap)

            if node1 in visit:
                continue
            visit.add(node1)
            ans = time1

            for node2, time2 in adj[node1]:
                if node2 not in visit:
                    heapq.heappush(min_heap, [time1 + time2, node2])

        return ans if len(visit) == n else -1