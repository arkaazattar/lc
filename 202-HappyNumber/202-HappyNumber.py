# Last updated: 2/1/2026, 9:46:59 PM
1class Solution:
2    def isHappy(self, n: int) -> bool: 
3        past_n = set()
4        while n != 1:
5            new_n = 0 
6            while n > 0:
7                new_n += (n % 10)**2
8                n = n // 10
9            n = new_n
10            if n not in past_n:
11                past_n.add(n)
12            else:
13                return False
14        return True