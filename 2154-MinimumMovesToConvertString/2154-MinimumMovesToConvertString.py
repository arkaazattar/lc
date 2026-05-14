# Last updated: 5/14/2026, 4:55:52 PM
class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)

        count = 0
        sweep = 0
        while sweep < length:
            if s[sweep] == 'X':
                count += 1
                sweep += 3

            else:
                sweep += 1
                
        return count