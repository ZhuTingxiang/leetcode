class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        elif n == 1 :
            return 1
        elif n == 2:
            return 2
        else:
            return climbStairs(n-1)+climbStairs(n-2)
        