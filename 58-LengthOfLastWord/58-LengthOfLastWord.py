# Last updated: 5/23/2026, 2:33:45 PM
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()

        return len(words[len(words) - 1])