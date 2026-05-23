# Last updated: 5/23/2026, 2:33:41 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        single = head
        double = head

        while double and double.next:
            single = single.next
            double = double.next.next
            
            if single == double:
                return True
        return False