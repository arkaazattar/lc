# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:        
        dummy = ListNode(-101, head)
        prev = dummy
        cur = head

        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if prev.next == cur:
                prev = cur
            else:
                prev.next = cur.next
            
            cur = cur.next
            
        return dummy.next
