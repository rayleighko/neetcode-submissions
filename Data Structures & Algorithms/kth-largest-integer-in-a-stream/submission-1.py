class KthLargest:
    # day 1 - only use my effort - use sorting, 
    # Time complexity: O(m∗nlogn)
    # Space complexity: O(m) extra space, O(1) or O(n) space depending on the sorting algorithm.
    # def __init__(self, k: int, nums: List[int]):
    #     self.stream = nums
    #     self.kth = k

    # def add(self, val: int) -> int:
    #     self.stream.append(val)
    #     return sorted(self.stream)[-self.kth]

    #     # another solution with solution video
    #     self.stream.append(val)
    #     self.stream.sort()
    #     return self.stream[len(self.stream) - self.kth]

    # day 1 - watch solution - use min heap
    # Time complexity: O(m∗logk)
    # Space complexity: O(k)
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]