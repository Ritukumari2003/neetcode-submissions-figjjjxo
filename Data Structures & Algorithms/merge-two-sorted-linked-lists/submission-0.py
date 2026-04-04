# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Brute force Approach
        if not list1 and not list2:
            return None
        arr = []
        while list1:
            arr.append(list1.val)
            list1 = list1.next
        while list2:
            arr.append(list2.val)    
            list2 = list2.next

        arr.sort()
        head = ListNode(arr[0]) 
        new_node = head
        for i in range(1,len(arr)):
            temp = ListNode(arr[i])
            new_node.next = temp
            new_node = new_node.next
        return head
        
        

            
            
            


        