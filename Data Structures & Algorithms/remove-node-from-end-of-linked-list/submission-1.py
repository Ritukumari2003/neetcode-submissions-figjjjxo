# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two pointer approach
        dummy = ListNode(0)
        dummy.next = head

        first = head
        second = dummy

        if head is None:
            return head
        if head.next is None:
            if n == 1:
                return None

        while n>0:
            first = first.next
            n -= 1
        while first:
            second = second.next
            first = first.next

        second.next = second.next.next

        return dummy.next
        

