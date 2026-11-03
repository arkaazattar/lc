# Last updated: 11/2/2026, 7:22:21 PM
1class Solution:
2    def detectCapitalUse(self, word: str) -> bool:
3
4        if len(word) == 1:
5            return True
6        
7        upper = word[0].isupper()
8
9        if upper:
10            if word[1].isupper():
11                for char in word[2:]:
12                    if not char.isupper():
13                        return False
14            
15            else:
16                for char in word[2:]:
17                    if char.isupper():
18                        return False
19        
20        else:
21            for char in word[1:]:
22                if char.isupper():
23                    return False
24
25        return True
26