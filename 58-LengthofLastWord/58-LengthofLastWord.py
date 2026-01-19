# Last updated: 1/19/2026, 12:21:51 AM
1class Solution(object):
2    def lengthOfLastWord(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        words = s.split()
8
9        return len(words[len(words) - 1])