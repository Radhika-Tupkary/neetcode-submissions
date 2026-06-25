# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointers = set()

        while head != None:
            if head in pointers:
                return True
            pointers.add(head)
            head = head.next
            
        return False