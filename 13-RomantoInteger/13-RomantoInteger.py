# Last updated: 1/22/2026, 7:33:56 PM
1class Solution:
2    def romanToInt(self, s: str) -> int:
3        values = {
4            'I' : 1,
5            'V' : 5,
6            'X' : 10,
7            'L' : 50,
8            'C' : 100,
9            'D' : 500,
10            'M' : 1000
11        }
12        seen = None
13        value = 0
14
15        for char in s:
16            if seen and values[char] > values[seen]:
17                value += values[char] - 2 * values[seen]
18            else: 
19                value += values[char]
20            seen = char
21        return value