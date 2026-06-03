# Last updated: 6/3/2026, 5:34:21 PM
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        rsp = []
4
5        for i in range(n + 1):
6
7            temp = i
8            bin_rep = ""
9            while temp > 0:
10                bin_rep = str(temp % 2) + bin_rep
11                temp //= 2
12            
13            rsp.append(bin_rep.count("1"))
14        
15        return rsp