"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}

        cur = head
        while cur:
            newNode = ListNode(val=cur.val)
            old_to_new[cur] = newNode
            cur = cur.next

        for old, cur in old_to_new.items():
            cur.next = old_to_new[old.next] if old.next else None
            cur.random = old_to_new[old.random] if old.random else None

        return old_to_new[head] if head else None
