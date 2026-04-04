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

    def reorderList(self, head: Optional[ListNode]) -> None:
        # Optimal Approach : TC : O(n) and SC : O(1)
        if not head:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next             
        rev_head = self.reverse_list(slow.next)
        slow.next = None
        temp = rev_head
        curr = head
        while temp:
            first = curr.next
            second = temp.next

            curr.next = temp
            temp.next = first
            
            curr = first
            temp = second
            

        
