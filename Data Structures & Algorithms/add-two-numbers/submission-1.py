# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
 
        dummy = ListNode(0)
        dummy_head = dummy

        carry = 0
        while temp1 and temp2:            
            node_sum = temp1.val + temp2.val + carry
            carry = node_sum // 10
            dummy.next = ListNode(node_sum%10)
            dummy = dummy.next
            temp1 = temp1.next
            temp2 = temp2.next

        if temp1:
            while temp1:
                node_sum = temp1.val + carry
                carry = node_sum // 10
                dummy.next = ListNode(node_sum%10)
                dummy = dummy.next
                temp1 = temp1.next

        elif temp2:
            while temp2:
                node_sum = temp2.val + carry
                carry = node_sum // 10
                dummy.next = ListNode(node_sum%10)
                dummy = dummy.next
                temp2 = temp2.next
        
        if carry != 0:
            dummy.next = ListNode(carry)
            dummy = dummy.next
        
        head = dummy_head.next
        dummy_head.next = None

        return head

        # prev = None
        # curr = head
        # while curr:
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next
        # return prev


        