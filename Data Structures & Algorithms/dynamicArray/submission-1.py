class DynamicArray:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._size = 0
        self.arr = [0] * self._capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self._size == self._capacity:
            self.resize()
        self.arr[self._size] = n
        self._size += 1

    def popback(self) -> int:
        if self._size > 0:
            self._size -= 1
        return self.arr[self._size]

    def resize(self) -> None:
        self._capacity *= 2
        new_arr = [0] * self._capacity

        for i in range(self._size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self._size
    
    def getCapacity(self) -> int:
        return self._capacity
