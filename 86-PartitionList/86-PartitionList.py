# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        left_dummy = ListNode()
        right_dummy = ListNode()

        left, right = left_dummy, right_dummy

        cur = head

        while cur:
            if cur.val >= x:
                right.next = cur
                right = right.next
            else:
                left.next = cur
                left = left.next
            
            cur = cur.next
        
        right.next = None
        left.next = right_dummy.next

        return left_dummy.next
