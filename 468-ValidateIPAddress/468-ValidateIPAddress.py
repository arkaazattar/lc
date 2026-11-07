# Last updated: 11/7/2026, 1:47:58 AM
1class Solution:
2    def validIPAddress(self, queryIP: str) -> str:
3        ipv4 = queryIP.split(".")
4        ipv6 = queryIP.split(":")
5        valid_ipv4, valid_ipv6 = True, True
6
7        if len(ipv4) != 4:
8            valid_ipv4 = False
9        
10        if len(ipv6) != 8:
11            valid_ipv6 = False
12
13        if not valid_ipv6 and not valid_ipv4:
14            return "Neither" 
15
16        if valid_ipv4:
17            for segment in ipv4:
18                if len(segment) > 4:
19                    return "Neither"
20                if segment > "255":
21                    return "Neither"
22                if not segment.isnumeric():
23                    return "Neither"
24                if segment[0] == '0' and len(segment) != 1:
25                    return "Neither"
26            return "IPv4"
27
28        elif valid_ipv6:
29            for segment in ipv6:
30                if len(segment) > 4 or len(segment) == 0:
31                    return "Neither"
32
33                for ch in segment:
34                    if ch not in "0123456789abcdefABCDEF":
35                        return "Neither"
36
37            return "IPv6"
38            
39        