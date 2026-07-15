# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2  = l1, l2
        head = None
        tail = None
        carry, result = 0, 0

        while cur1 or cur2 or carry:
            if cur1 and cur2:
                total = cur1.val + cur2.val + carry                
            elif cur1:
                total = cur1.val + carry
            elif cur2:
                total = cur2.val + carry
            else:
                total = carry

            if total < 10:
                carry = 0
                result = total
            else:
                carry = total // 10
                result = total % 10

            node = ListNode(val=result)

            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None

            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node

        return head

        
        

