# Last updated: 5/15/2026, 5:39:32 PM
1class Solution:
2    def reverseWords(self, s: str) -> str:
3        last_word = ""
4        arr = []
5
6        for ch in s:
7            if ch != " ":
8                last_word += ch
9            
10            elif last_word:
11                arr.append(last_word)
12                last_word = ""
13        
14        if last_word:
15            arr.append(last_word)
16        arr.reverse()
17        return " ".join(arr)
18        
19
20            
21
22
23
24