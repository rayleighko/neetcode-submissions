class DynamicArray:
    def __init__(self, capacity: int):
        self.arr = []
        self._size = 0
        self._capacity = capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        self.arr.append(n)
        self._size += 1
        if self._size > self._capacity:
            self.resize()

    def popback(self) -> int:
        self._size -= 1
        return self.arr.pop()

    def resize(self) -> None:
        self._capacity *= 2

    def getSize(self) -> int:
        return self._size
    
    def getCapacity(self) -> int:
        return self._capacity
