# Last updated: 5/22/2026, 10:32:48 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        last_word = ""
        arr = []

        for ch in s:
            if ch != " ":
                last_word += ch
            
            elif last_word:
                arr.append(last_word)
                last_word = ""
        
        if last_word:
            arr.append(last_word)
        arr.reverse()
        return " ".join(arr)
        

            



