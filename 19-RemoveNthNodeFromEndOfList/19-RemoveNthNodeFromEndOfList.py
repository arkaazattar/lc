# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        cur = head
        nodes = []
        dummy = ListNode(0, head)
        nodes.append(dummy)
        while cur:
            nodes.append(cur)
            cur = cur.next

        if n == len(nodes) - 1:
            dummy.next = dummy.next.next
        else:
            nodes[len(nodes) - 1 - n].next = nodes[len(nodes) - 1 - n].next.next if nodes[len(nodes) - 1 - n].next.next else None  
        
        return dummy.next
