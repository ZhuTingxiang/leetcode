class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # result = 1
        # if n == 0:
        #     return 1
        # for i in range(1,n+1):
        #     result *= x
        #     i += 1
        # return result
        return pow(x,n)