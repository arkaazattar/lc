# Last updated: 5/23/2026, 2:33:51 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        seen = None
        value = 0

        for char in s:
            if seen and values[char] > values[seen]:
                value += values[char] - 2 * values[seen]
            else: 
                value += values[char]
            seen = char
        return value