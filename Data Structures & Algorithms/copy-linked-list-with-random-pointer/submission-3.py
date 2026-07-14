class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        p1 = head
        cur1 = Node(x=p1.val)
        result = cur1
        p2 = head.next
        mapping = {}

        while p1:
            mapping[p1] = cur1
            if p2:
                cur2 = Node(x=p2.val)
                cur1.next = cur2
                cur1 = cur2
            p1 = p2
            p2 = p2.next if p2 else None

        p1 = head
        cur1 = result

        while p1:
            if p1.random:
                cur1.random = mapping[p1.random] 
            p1 = p1.next
            cur1 = cur1.next

        return result