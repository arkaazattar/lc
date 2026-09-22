# Last updated: 9/22/2026, 6:39:06 PM
1class Solution:
2    def myAtoi(self, s: str) -> int:
3        rsp = 0
4        digits = []
5        pos = [False, True]
6        integers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'} 
7        high, low = 2**31 - 1, -2**31
8
9
10        for char in s:
11            if not digits and not pos[0] and char == ' ':
12                continue
13
14            elif not digits and char in '-+':
15                if pos[0]:
16                    break
17                pos[0] = True
18                
19                if char == '-':
20                    pos[1] = False
21                
22                elif char == '+':
23                    pos[0] == True
24            
25            elif char not in integers:
26                break
27
28            else:
29                digits.append(char)
30            
31        n = len(digits)
32        for i in range(len(digits)):
33            if not rsp and digits[i] == '0':
34                continue
35            
36            elif digits[i] == 0:
37                break
38            
39            else:
40                rsp += int(digits[i]) * 10**(n - i - 1)
41            
42
43        if not pos[1]:
44            rsp *= -1
45
46        if rsp > high:
47            rsp = high
48
49        elif rsp < low:
50            rsp = low
51            
52        return rsp