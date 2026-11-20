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
            if old.next:
                new.next = old_to_new[old.next]

            if old.random:
                new.random = old_to_new[old.random]

        return old_to_new[head] if head else None
