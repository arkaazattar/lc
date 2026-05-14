# Last updated: 5/14/2026, 4:56:01 PM
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()

        return len(words[len(words) - 1])