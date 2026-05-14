# Last updated: 5/14/2026, 4:55:55 PM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        target = {}
        
        for char in ransomNote:
            if target.get(char):
                target[char] += 1
            else:
                target[char] = 1

        for char in magazine:
            if target.get(char):
                target[char] -= 1
    
        if sum(target.values()) == 0:
            return True
        return False