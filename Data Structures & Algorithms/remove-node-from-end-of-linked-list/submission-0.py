# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        p2 = dummy
        p1 = head

        for i in range(n-1):
            p1 = p1.next

        while p1.next != None:
            p2 = p2.next
            p1 = p1.next

        result_node = p2.next
        p2.next = p2.next.next
        result_node.next = None

        return dummy.next

        