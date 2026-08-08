# Last updated: 8/8/2026, 2:56:58 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rsp = ListNode()
        curr = rsp
        carry = 0
        l1_ptr, l2_ptr = l1, l2

        while l1_ptr or l2_ptr or carry:
            v1 = l1_ptr.val if l1_ptr else 0
            v2 = l2_ptr.val if l2_ptr else 0

            v3 = v1 + v2 + carry
            curr.next = ListNode(v3 % 10)
            carry = v3 // 10
            curr = curr.next
            
            l1_ptr = l1_ptr.next if l1_ptr else None
            l2_ptr = l2_ptr.next if l2_ptr else None
            
        return rsp.next
