# Last updated: 6/4/2026, 1:09:54 PM
class Solution:
    def fib(self, n: int) -> int:
        f = [0 , 1]
        
        if n == 0:
            return 0

        for i in range(2, n + 1):
            f.append(f[i - 2] + f[i - 1])
            
        return f[-1]
