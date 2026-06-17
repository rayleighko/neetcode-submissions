class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)

        i = len(self.heap) - 1
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2

    def pop(self) -> int:
        if not self.heap or len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]

        self.heap[1] = self.heap.pop()
        
        i = 1
        while 2 * i < len(self.heap):
            l, r = 2 * i, 2 * i + 1
            if r < len(self.heap) and self.heap[r] < self.heap[l] and self.heap[i] > self.heap[r]:
                tmp = self.heap[r]
                self.heap[r] = self.heap[i]
                self.heap[i] = tmp
                i = r
            elif self.heap[i] > self.heap[l]:
                tmp = self.heap[l]
                self.heap[l] = self.heap[i]
                self.heap[i] = tmp
                i = l
            else:
                break

        return res

    def top(self) -> int:
        if not self.heap or len(self.heap) == 1:
            return -1

        return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            i = cur
            while 2 * i < len(self.heap):
                l, r = 2 * i, 2 * i + 1
                if r < len(self.heap) and self.heap[r] < self.heap[l] and self.heap[i] > self.heap[r]:
                    tmp = self.heap[r]
                    self.heap[r] = self.heap[i]
                    self.heap[i] = tmp
                    i = r
                elif self.heap[i] > self.heap[l]:
                    tmp = self.heap[l]
                    self.heap[l] = self.heap[i]
                    self.heap[i] = tmp
                    i = l
                else:
                    break
            cur -= 1

        