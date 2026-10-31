# Last updated: 10/31/2026, 6:30:01 PM
class Solution:
    def myAtoi(self, s: str) -> int:
        rsp = 0
        digits = []
        pos = [False, True]
        integers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'} 
        high, low = 2**31 - 1, -2**31


        for char in s:
            if not digits and not pos[0] and char == ' ':
                continue

            elif not digits and char in '-+':
                if pos[0]:
                    break
                pos[0] = True
                
                if char == '-':
                    pos[1] = False
                
                elif char == '+':
                    pos[0] == True
            
            elif char not in integers:
                break

            else:
                digits.append(char)
            
        n = len(digits)
        for i in range(len(digits)):
            if not rsp and digits[i] == '0':
                continue
            
            elif digits[i] == 0:
                break
            
            else:
                rsp += int(digits[i]) * 10**(n - i - 1)
            

        if not pos[1]:
            rsp *= -1

        if rsp > high:
            rsp = high

        elif rsp < low:
            rsp = low
            
        return rsp