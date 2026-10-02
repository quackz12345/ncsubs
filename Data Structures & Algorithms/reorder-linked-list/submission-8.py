# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        if(not head):
            head = ListNode()
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        curr = mid
        prev = None
        while curr:
            nexts = curr.next
            curr.next = prev
            prev = curr
            curr = nexts
        mid = prev
        curr = head
        while curr != mid and curr.next != mid:
            nexts = curr.next
            curr.next = mid

            mnext = mid.next
            mid.next = nexts

            curr = nexts
            mid = mnext
        
        
        