# Last updated: 10/31/2026, 6:28:45 PM
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        rsp_set = set()
        n = len(digits)

        for first_digit in range(n):
            for second_digit in range(n):
                for third_digit in range(n):
                    if first_digit == second_digit or second_digit == third_digit or first_digit == third_digit:
                        continue
                    number = int(str(digits[first_digit]) + str(digits[second_digit]) + str(digits[third_digit]))
                    
                    
                    if 99 < number < 1000 and number not in rsp_set and number % 2 == 0:
                        rsp_set.add(number) 
        
        return len(rsp_set) 