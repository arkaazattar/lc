# Last updated: 5/23/2026, 2:33:36 PM
class Solution:
    def isHappy(self, n: int) -> bool: 
        past_n = set()
        while n != 1:
            new_n = 0 
            while n > 0:
                new_n += (n % 10)**2
                n = n // 10
            n = new_n
            if n not in past_n:
                past_n.add(n)
            else:
                return False
        return True