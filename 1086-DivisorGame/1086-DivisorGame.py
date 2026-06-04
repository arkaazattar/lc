# Last updated: 6/4/2026, 3:38:19 PM
class Solution:
    def divisorGame(self, n: int) -> bool:
        # if n is odd, then the number can be forced to be odd 
        # and force a loser.
        # ex. n = 5
        # 5 Alice
        # 4 Bob
        # 3 Alice
        # 2 Bob
        # 1 Alice
        # so if n is even, alice will win assuming she plays optimally and is first

        return n % 2 == 0 