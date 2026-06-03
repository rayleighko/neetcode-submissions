# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # day 1 - only my effort, this solution's Space complexity is O(n+m)
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        # day 1 - watch solution, use Iteration this solution's Space complexity is O(1)
        # two solution's Time complexity is same = O(n + m)
        # dummy = node = ListNode()

        # while list1 and list2:
        #     if list1.val < list2.val:
        #         node.next = list1
        #         list1 = list1.next
        #     else:
        #         node.next = list2
        #         list2 = list2.next
        #     node = node.next

        # node.next = list1 or list2

        # return dummy.next