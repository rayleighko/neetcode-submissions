class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.size = 0
        
    def get(self, index: int) -> int:
        if self.size <= index:
            return -1

        curr = self.head.next
        for _ in range(index):
            print(curr.val)
            curr = curr.next

        print(curr)
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        print(val)
        node = ListNode(val)

        node.next = self.head.next
        self.head.next = node
        self.size += 1
         
    def addAtTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next

        node = ListNode(val)
        curr.next = node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if self.size < index:
            return
            
        curr = self.head
        for _ in range(index):
            curr = curr.next

        node = ListNode(val)
        node.next = curr.next
        curr.next = node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if self.size <= index:
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next

        curr.next = curr.next.next
            
        self.size -= 1