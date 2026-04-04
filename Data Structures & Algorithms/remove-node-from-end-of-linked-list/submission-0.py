# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_list(self, head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = self.reverse_list(head)

        if not head:
            return head
        if head.next is None:
            if n == 1:
                return None

        prev = None
        curr = head
        if n == 1:
            head = head.next  
            curr.next = None
            return self.reverse_list(head) 
        
        while curr and n-1!=0:
            prev = curr
            curr = curr.next
            n -= 1
        prev.next = curr.next
        curr.next = None

        return self.reverse_list(head)


        