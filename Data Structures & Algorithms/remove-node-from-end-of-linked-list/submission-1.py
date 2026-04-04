# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def reverse_list(self, head):
    #     prev = None
    #     curr = head
    #     while curr:
    #         next = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = next
    #     return prev
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # head = self.reverse_list(head)

        # if not head:
        #     return head
        # if head.next is None:
        #     if n == 1:
        #         return None

        # prev = None
        # curr = head
        # if n == 1:
        #     head = head.next  
        #     curr.next = None
        #     return self.reverse_list(head) 
        
        # while curr and n-1!=0:
        #     prev = curr
        #     curr = curr.next
        #     n -= 1
        # prev.next = curr.next
        # curr.next = None

        # return self.reverse_list(head)
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
        

