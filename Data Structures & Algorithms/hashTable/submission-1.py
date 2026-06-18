class Pair:
    def __init__(self, key=None, val=None, nxt=None):
        self.key, self.val, self.next = key, val, nxt

class HashTable:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = [None] * self.capacity

    def hash(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
        cur = self.map[index]

        if not cur:
            self.map[index] = Pair(key, value)
            self.size += 1
        else:
            prev = None
            while cur:
                if cur.key == key:
                    cur.val = value
                    return
                prev, cur = cur, cur.next
            prev.next = Pair(key, value)
            self.size += 1

        # if self.size > self.capacity // 2:
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash(key)
        cur = self.map[index]

        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next

        return -1

    def remove(self, key: int) -> bool:
        index = self.hash(key)
        cur = self.map[index]
        prev = None

        while cur:
            if cur.key == key:
                if prev:
                    prev.next = cur.next
                else:
                    self.map[index] = cur.next
                self.size -= 1
                return True
            prev, cur = cur, cur.next
        
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        newCapacity = self.capacity * 2
        newMap = [None] * newCapacity

        for pair in self.map:
            while pair:
                index = pair.key % newCapacity
                if newMap[index] is None:
                    newMap[index] = Pair(pair.key, pair.val)
                else:
                    newPair = newMap[index]
                    while newPair.next:
                        newPair = newPair.next
                    newPair.next = Pair(pair.key, pair.val)
                pair = pair.next
        
        self.capacity = newCapacity
        self.map = newMap

