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
            cur = cur.next

        k = k % num_nodes
        # 0 indexed
        tail = num_nodes - k - 1
        
        tail_ptr = head
        for _ in range(tail):
            tail_ptr = tail_ptr.next

        new_head = tail_ptr.next if tail_ptr.next else head
        tail_ptr.next = None

        if new_head == head:
            return new_head
        
        cur = new_head
        while cur.next:
            cur = cur.next
        cur.next = head

        return new_head
