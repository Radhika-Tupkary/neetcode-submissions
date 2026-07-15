# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = l1
        list1 = []
        while cur:
            list1.append(str(cur.val))
            cur = cur.next
        cur = l2
        list2 = []
        while cur:
            list2.append(str(cur.val))
            cur = cur.next
        list1.reverse()
        list2.reverse()
        num1 = "".join(list1)
        num2 = "".join(list2)
        result = int(num1) + int(num2)

        head = None
        tail = None

        for num in reversed(list(str(result))):
            node = ListNode(val=num)
            
            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node
        
        return head
        
        

