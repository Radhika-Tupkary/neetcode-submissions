# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find total nodes
        p1 = head
        count = 0
        while p1:
            count += 1
            p1 = p1.next
        
        print("total nodes:", count)
        if count == 1:
            return

        # 2. find middle
        i = 1
        p2 = head
        while i < (count//2 + count % 2):
            p2 = p2.next
            i += 1

        # 3. split the list
        second_list_starting = p2.next
        p2.next = None

        print("first list ending:", p2.val)
        print("second list starting:", second_list_starting.val)

        # 4. reverse the second list
        dummy = ListNode()
        cur = second_list_starting
        cur2 = second_list_starting

        while cur:
            cur2 = cur.next
            cur.next = dummy
            dummy = cur
            cur = cur2
        
        second_list_starting.next = None

        # 5. merge two lists l1 and l2
        l1 = head # first half of the original list
        l2 = dummy # reversed second half of the original list
        d1, d2 = None, None

        while l1 or l2:
            if l1:
                d1 = l1.next
                l1.next = l2
            if l2:
                d2 = l2.next
                l2.next = d1
            l1 = d1
            l2 = d2
            
            




        





        