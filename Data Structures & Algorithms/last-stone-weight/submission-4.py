class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # day 1 - watch solution
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)
            else:
                heapq.heappush(stones, second - first)
        
        return abs(heapq.heappop(stones)) if stones else 0