# Last updated: 5/23/2026, 2:33:52 PM
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False

        reversed = 0
        temp = x

        while temp != 0:
            
            reversed = (reversed * 10) + (temp % 10)
            temp //= 10
        
        return reversed == x