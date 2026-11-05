# Last updated: 11/5/2026, 1:39:11 AM
1class Solution:
2    def complexNumberMultiply(self, num1: str, num2: str) -> str:
3        # seperate real and imaginary parts
4        real1, imaginary1 = num1.split("+")
5        real2, imaginary2 = num2.split("+")
6        
7        # convert values to int
8        real1, real2 = int(real1), int(real2)
9        imaginary1, imaginary2 = int(imaginary1[:-1]), int(imaginary2[:-1])
10
11        real_part = real1 * real2 - imaginary1 * imaginary2
12        imaginary_part = real1 * imaginary2 + real2 * imaginary1
13
14        return f"{real_part}+{imaginary_part}i"
15        
16
17        return rsp