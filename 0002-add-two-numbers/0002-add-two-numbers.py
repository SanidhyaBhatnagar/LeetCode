class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        c1 = l1
        c2 = l2

        dummy = ListNode(0)
        c3 = dummy

        carry = 0

        while c1 is not None or c2 is not None or carry != 0:

            if c1 is not None:
                val1 = c1.val
            else:
                val1 = 0

            if c2 is not None:
                val2 = c2.val
            else:
                val2 = 0

            add = val1 + val2 + carry

            digit = add % 10
            carry = add // 10

            new = ListNode(digit)

            c3.next = new
            c3 = c3.next

            if c1 is not None:
                c1 = c1.next

            if c2 is not None:
                c2 = c2.next

        return dummy.next