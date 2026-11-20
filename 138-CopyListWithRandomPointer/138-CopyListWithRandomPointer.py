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
        # create nodes
        old_to_new = {}
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        for old, new in old_to_new.items():
            if old and old.next:
                new.next = old_to_new[old.next]
            else:
                new.next = None
            if old and old.random:
                new.random = old_to_new[old.random]
            else:
                new.random = None
        for old, new in old_to_new.items():
            return new
