# Last updated: 9/11/2026, 2:38:26 PM
1class Solution:
2    def totalNumbers(self, digits: List[int]) -> int:
3        rsp_set = set()
4        n = len(digits)
5
6        for first_digit in range(n):
7            for second_digit in range(n):
8                for third_digit in range(n):
9                    if first_digit == second_digit or second_digit == third_digit or first_digit == third_digit:
10                        continue
11                    number = int(str(digits[first_digit]) + str(digits[second_digit]) + str(digits[third_digit]))
12                    
13                    
14                    if 99 < number < 1000 and number not in rsp_set and number % 2 == 0:
15                        rsp_set.add(number) 
16        
17        return len(rsp_set) 