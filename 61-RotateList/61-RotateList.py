# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head:
            return head

        num_nodes = 0
        cur = head
        while cur:
            num_nodes += 1
            original_tail = cur
            cur = cur.next
        

        k %= num_nodes
        if k == 0:
            return head
        
        new_tail_index = num_nodes - k - 1
        
        tail = head
        for _ in range(new_tail_index):
            tail = tail.next

        new_head = tail.next
        tail.next = None
        original_tail.next = head
        
        return new_head
