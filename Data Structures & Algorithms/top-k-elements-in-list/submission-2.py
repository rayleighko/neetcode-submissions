class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        min_heap = []
        for n in count.keys():
            heapq.heappush(min_heap, (count[n], n))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        
        return res