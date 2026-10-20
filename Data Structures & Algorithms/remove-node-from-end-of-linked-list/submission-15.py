class Solution:
    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def remove(self, head, n):
        if n == 1:
            head.next = head.next.next
            return

        self.remove(head.next, n - 1)

    def removeNthFromEnd(self, head, n):
        # Reverse
        head = self.reverse(head)

        # Dummy handles removing the first node
        dummy = ListNode(0, head)

        # Remove nth node from beginning
        self.remove(dummy, n)

        # Reverse again
        return self.reverse(dummy.next)