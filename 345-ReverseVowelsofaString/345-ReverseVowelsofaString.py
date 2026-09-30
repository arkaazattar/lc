# Last updated: 9/30/2026, 7:55:01 PM
1class Solution:
2    def reverseVowels(self, s: str) -> str:
3        l, r = 0, len(s) - 1
4        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
5        
6        s = list(s)
7
8        while l < r:
9            if s[l] in vowels and s[r] in vowels:
10                s[l], s[r] = s[r], s[l]
11                l += 1
12                r -= 1
13            
14            elif s[l] in vowels and s[r] not in vowels:
15                r -= 1
16            
17            elif s[l] not in vowels and s[r] in vowels:
18                l += 1
19            
20            else:
21                l += 1
22                r -= 1
23
24        return "".join(s)