class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a, b = 1, 2
            
            for i in range(2,n):
                temp = a
                a = b
                b = temp + b
                i += 1
            return b