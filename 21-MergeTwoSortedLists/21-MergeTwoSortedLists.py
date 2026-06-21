# Last updated: 6/20/2026, 10:27:28 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return
        
        rsp = ListNode()
        l1_ptr, l2_ptr, rsp_ptr = list1, list2, rsp 

        while l1_ptr or l2_ptr:
            if not l1_ptr:
                rsp_ptr.val = l2_ptr.val
                l2_ptr = l2_ptr.next
            
            elif not l2_ptr:
                rsp_ptr.val = l1_ptr.val
                l1_ptr = l1_ptr.next
            
            elif l1_ptr.val < l2_ptr.val:
                rsp_ptr.val = l1_ptr.val
                l1_ptr = l1_ptr.next

            else:
                rsp_ptr.val = l2_ptr.val
                l2_ptr = l2_ptr.next

            if l1_ptr or l2_ptr:
                rsp_ptr.next = ListNode()
                rsp_ptr = rsp_ptr.next


        return rsp