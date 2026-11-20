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
        cur = head
        old_to_new = {}
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next
        # now have a dict where old nodes have corresponding new nodes that are not linked
        for old, new in old_to_new.items():
            # give its next
            if old.next:
                new.next = old_to_new[old.next]
            # give its random
            if old.random:
                new.random = old_to_new[old.random]

        return old_to_new[head] if head else None
