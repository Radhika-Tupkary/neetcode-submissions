class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        # 1. Find middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split list
        second = slow.next
        slow.next = None


        # 3. Reverse second half
        prev = None
        cur = second

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        second = prev


        # 4. Merge two halves
        first = head

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2